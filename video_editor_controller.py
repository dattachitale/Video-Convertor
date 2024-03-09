import configparser
import csv
import ctypes
import json
import os
import pickle
import subprocess
import sys
import time
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from datetime import timedelta, datetime

import psutil
import win32con
import win32gui
from PySide6.QtCore import QThread
from PySide6.QtGui import QIcon, QPixmap

import style_sheet
import video_editor_UI
from videoX import VideoX
from video_player import VideoPlayer
from message_box import MessageBox
from output_format_msgbox import OutputFormatMsgBox
# from authenticate_me import AuthenticateMe
# from elastic_server_connector import ElasticServerConnector

# from elastic_server_connector import ElasticServerConnector

'''Main class'''


# noinspection PyAttributeOutsideInit
class videoController(video_editor_UI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(videoController, self).__init__()
        self.userName = os.getlogin()
        # self.userID = userEmailID
        self.bitrateReductionSpinBox = None
        self.setupUi(self)
        self.hideMenubar()
        self.setAcceptDrops(True)
        self.extList = ['avi', 'wmv', 'mp4', 'mkv', 'flv']
        self.extensions = ' '.join([f'*.{ext}' for ext in self.extList])
        self.defaultOutputDir = 'Converted_Videos\\'

        self.vPlayer = None
        self.helpURL = "https://confluence.ubisoft.com/pages/viewpage.action?pageId=1464435025"

        self.dragUrl = ''
        self.dragUrlExt = ''

        # Flags
        self.interrupted = False
        self.firstTrigger = True

        # Data Collection Counters
        # Counts
        self.initCounts()

        # Config/Output Variables
        self.DURATION = ''
        self.START = ''
        self.END = ''
        self.FPS = ''
        self.BITRATE = ''
        self.RESOLUTION = ''
        self.AUDIO = True
        self.FMT = ''
        self.TARGETFILESIZEMB = ''
        self.COMMAND = ''

        # Create separate parser for elasticsearch settings
        # self.elasticsearchConfigfile = "elasticsearch_config.ini"
        # self.elasticsearchConfig = configparser.ConfigParser()
        # self.elasticsearchConfig.read(self.elasticsearchConfigfile)
        # self.videoEditorIndex = str(self.elasticsearchConfig["index-name"]["video_editor_stats"])
        #
        # # ElasticServerDLL
        # self.elasticObj = ElasticServerConnector(userID='sourabh.desai@ubisoft.com',
        #                                          appName='PunAutomation_VideoEditorTool')

        # Default Output Directory
        if not os.path.exists(self.defaultOutputDir):
            os.makedirs(self.defaultOutputDir)
        self.outputPathDirectory = os.path.join(os.getcwd(), self.defaultOutputDir)
        self.outputPathLineEdit.setText(self.outputPathDirectory)
        self.outputPathLineEdit.setToolTip(self.outputPathDirectory)

        # Button connections
        self.selectVideoButton.clicked.connect(self.selectVidFile)
        self.closeButton.clicked.connect(self._close)
        self.minimizeButton.clicked.connect(self.minimizeWindow)
        self.helpButton.clicked.connect(self.openHelp)
        self.setOutputPathButton.clicked.connect(self.setOutputPath)
        self.provideSizeLineEdit.textChanged.connect(self.disableOutputSetting)
        self.convertVideoButton.clicked.connect(self.checkOutputFormat)
        self.infoplayVideoButton.clicked.connect(self.play)
        self.trimVideoButton.clicked.connect(self.trimVideo)
        self.saveConfigButton.clicked.connect(self.saveConfig)
        self.loadConfigButton.clicked.connect(self.loadConfig)

        # Mouse Move Event
        self.mainFrame.mouseMoveEvent = self.moveWindow

        # Video File Object
        self.vidFileObj = None

        # Messagebox Object
        self.messagebox = None

        # Keep Config Variables updated
        self.startTimeLineEdit.textChanged.connect(self.updateSTART)
        self.endTimeLineEdit.textChanged.connect(self.updateEND)
        self.bitrateReductionSpinBox.textChanged.connect(self.updateBITRATE)
        self.fpsSpinBox.textChanged.connect(self.updateFPS)
        self.resolutionComboBox.currentTextChanged.connect(self.updateRESOLUTION)
        self.keepAudioCheckBox.clicked.connect(self.updateAUDIO)
        self.provideSizeLineEdit.editingFinished.connect(self.updateTARGETFILESIZEMB)
        self.aviRadioButton.clicked.connect(self.updateFMT)
        self.mp4RadioButton.clicked.connect(self.updateFMT)
        self.wmvRadioButton.clicked.connect(self.updateFMT)

        self.modifiedAttributes = {
            'START': self.START,
            'END': self.END,
            'FPS': self.FPS,
            'BITRATE': self.BITRATE,
            'RESOLUTION': self.RESOLUTION,
            'AUDIO': self.AUDIO,
            'FMT': self.FMT,
            'TARGETFILESIZEMB': self.TARGETFILESIZEMB,
            'OUTPUTPATH': self.outputPathDirectory
        }

        print(f'INIT MODIFIED_ATTRIBUTES:{self.modifiedAttributes}')

    def initCounts(self):

        self.toolTriggered = 1 if self.firstTrigger else 0

        self.countSucceeded = 0
        self.countFailed = 0
        self.countFrameRate = 0
        self.countTargetSize = 0
        self.countBitrate = 0
        self.countResolution = 0
        self.countsaveConfig = 0
        self.countLoadConfig = 0
        self.countTrim = 0
        self.countAudioRemove = 0
        self.countMP4 = 0
        self.countWMV = 0
        self.countAVI = 0
        self.countTrim = 0
        self.countSaveConfig = 0
        self.countLoadConfig = 0

    def updateCounts(self):
        self.firstTrigger = False
        self.countSucceeded += 1
        if not self.modifiedAttributes['AUDIO']:
            self.countAudioRemove += 1
        if self.modifiedAttributes['TARGETFILESIZEMB']:
            self.countTargetSize += 1
        if self.modifiedAttributes['BITRATE']:
            self.countBitrate += 1
        if self.modifiedAttributes['RESOLUTION']:
            self.countResolution += 1
        if self.modifiedAttributes['FPS']:
            self.countFrameRate += 1
        if self.modifiedAttributes['FMT'] == '.mp4':
            self.countMP4 += 1
        if self.modifiedAttributes['FMT'] == '.wmv':
            self.countWMV += 1
        if self.modifiedAttributes['FMT'] == '.avi':
            self.countAVI += 1
        if (self.modifiedAttributes['START'] or self.modifiedAttributes['END']) and \
                (self.modifiedAttributes['START'] != "00:00:00" or self.modifiedAttributes[
                    'END'] != self.vidFileObj.duration):
            self.countTrim += 1

            self.videoStatsDict = {
                             'Trigger_Count': self.toolTriggered,
                             'Succeed_Count': self.countSucceeded,
                             'Removed_Audio': self.countAudioRemove,
                             'TargetSize_Count': self.countTargetSize,
                             'Bitrate_Count': self.countBitrate,
                             'Resolution_Count': self.countResolution,
                             'FPS_Count': self.countFrameRate,
                             'MP4_Count': self.countMP4,
                             'WMV_Count': self.countWMV,
                             'AVI_Count': self.countAVI,
                             'Trim_Count': self.countTrim,
                             'Save_Config_Count': self.countSaveConfig,
                             'Load_Config_Count': self.countLoadConfig
                             }
        _data = json.dumps(self.videoStatsDict)
        print(f"DATA:{_data}")
        # self.elasticObj.pushData(_data)

        # Reset the Counts
        self.initCounts()

    def updateSTART(self):
        _START = self.startTimeLineEdit.text()
        if _START or _START != "00:00:00":
            self.modifiedAttributes['START'] = _START
        else:
            self.modifiedAttributes['START'] = None

    def updateEND(self):
        _END = self.endTimeLineEdit.text()
        self.modifiedAttributes['END'] = _END if _END or _END != "00:00:00" else None

    def updateBITRATE(self):
        if self.bitrateReductionSpinBox.text() == 'Unset':
            self.modifiedAttributes['BITRATE'] = None
            self.fpsSpinBox.setEnabled(True)
            self.fpsSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxEnableSS)
        else:
            self.modifiedAttributes['BITRATE'] = (self.bitrateReductionSpinBox.text() or None)
            self.fpsSpinBox.setEnabled(False)
            self.fpsSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxDisableSS)

    def updateFPS(self):
        if self.fpsSpinBox.text() == 'Unset':
            self.modifiedAttributes['FPS'] = None
        else:
            self.modifiedAttributes['FPS'] = self.fpsSpinBox.text() or None

    def updateRESOLUTION(self):
        if self.resolutionComboBox.currentText() == 'Unset':
            self.modifiedAttributes['RESOLUTION'] = None
        else:
            self.modifiedAttributes['RESOLUTION'] = (self.resolutionComboBox.currentText() or None)

    def updateAUDIO(self):
        self.modifiedAttributes['AUDIO'] = bool(self.keepAudioCheckBox.isChecked())

    def updateTARGETFILESIZEMB(self):
        print(f'Current Minsize: {self.minSize}')
        if int(self.provideSizeLineEdit.text()) > self.minSize:
            self.modifiedAttributes['TARGETFILESIZEMB'] = (self.provideSizeLineEdit.text() or None)
        else:
            if self.messagebox:
                self.messagebox.close()
            self.messagebox = MessageBox('Warning',
                                         f'Please Provide Size Greater Than or Equal to \n {int(self.minSize) + 1} MB')
            self.messagebox.exec()
            self.provideSizeLineEdit.clear()

    def updateFMT(self):
        if self.mp4RadioButton.isChecked():
            self.modifiedAttributes['FMT'] = '.mp4'
        elif self.wmvRadioButton.isChecked():
            self.modifiedAttributes['FMT'] = '.wmv'
        elif self.aviRadioButton.isChecked():
            self.modifiedAttributes['FMT'] = '.avi'
        else:
            self.modifiedAttributes['FMT'] = None

    def setFMT(self):
        if self.modifiedAttributes['FMT'] == '.mp4':
            self.mp4RadioButton.setChecked(True)
        elif self.modifiedAttributes['FMT'] == '.wmv':
            self.wmvRadioButton.setChecked(True)
        elif self.modifiedAttributes['FMT'] == '.avi':
            self.aviRadioButton.setChecked(True)
        else:
            self.mp4RadioButton.setChecked(False)
            self.wmvRadioButton.setChecked(False)
            self.aviRadioButton.setChecked(False)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        self.dragUrl = str(urls[0].path())[1:]
        self.dragUrlExt = str(self.dragUrl.split('.')[-1])
        if self.dragUrlExt in self.extList:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if self.dragUrlExt in self.extList:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if self.dragUrlExt in self.extList:
            event.acceptProposedAction()
            self.vidFile = os.path.normpath(self.dragUrl)
            # Create Video Object
            self.initVidObj()
            self.enableAll()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def moveWindow(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            event.accept()
            self.dragPos = event.globalPosition().toPoint()

    def hideMenubar(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def initVidObj(self):
        self.vidFileObj = None
        self.vidFileObj = VideoX(self.vidFile)
        self.updateMetaData()

    def enableAll(self):
        self.convertVideoButton.setEnabled(True)
        self.convertVideoButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.loadConfigButton.setEnabled(True)
        self.loadConfigButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.saveConfigButton.setEnabled(True)
        self.saveConfigButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.trimVideoButton.setEnabled(True)
        self.trimVideoButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.startTimeLineEdit.setEnabled(True)
        self.startTimeLineEdit.setText("00:00:00")
        self.startTimeLineEdit.setStyleSheet(style_sheet.startEndTimeLineEditEnableSS)
        self.endTimeLineEdit.setEnabled(True)
        self.endTimeLineEdit.clear()
        self.endTimeLineEdit.setStyleSheet(style_sheet.startEndTimeLineEditEnableSS)
        self.provideSizeLineEdit.setEnabled(True)
        self.provideSizeLineEdit.clear()
        self.provideSizeLineEdit.setStyleSheet(style_sheet.provideSizeLineEditEnableSS)
        self.keepAudioCheckBox.setEnabled(True)
        self.keepAudioCheckBox.setStyleSheet(style_sheet.keepAudioCheckBoxEnableSS)
        self.targetSizeLabel.setEnabled(True)
        self.targetSizeLabel.setStyleSheet(style_sheet.infoAllLabel1SS)
        self.mp4RadioButton.setEnabled(True)
        self.wmvRadioButton.setEnabled(True)
        self.aviRadioButton.setEnabled(True)
        self.bitrateReductionSpinBox.setEnabled(True)
        self.bitrateReductionSpinBox.setValue(5)
        self.bitrateReductionSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxEnableSS)
        self.fpsSpinBox.setEnabled(True)
        self.fpsSpinBox.setValue(22)
        self.fpsSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxEnableSS)
        self.resolutionComboBox.setEnabled(True)
        self.resolutionComboBox.setCurrentIndex(0)
        self.resolutionComboBox.setStyleSheet(style_sheet.resolutionComboBoxEnableSS)
        self.infoplayVideoButton.setEnabled(True)
        self.infoplayVideoButton.setStyleSheet(style_sheet.infoplayVideoButtonEnableSS)

    # disable all output setting after user enters target size in MB
    def disableOutputSetting(self):
        if self.provideSizeLineEdit.text():
            self.bitrateReductionSpinBox.setEnabled(False)
            self.bitrateReductionSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxDisableSS)
            self.fpsSpinBox.setEnabled(False)
            self.fpsSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxDisableSS)
            self.resolutionComboBox.setEnabled(False)
            self.resolutionComboBox.setStyleSheet(style_sheet.resolutionComboBoxDisableSS)
        elif not self.provideSizeLineEdit.text():
            self.enableOutputSetting()

    # enable all output setting again if user does not enter anything in target size MB and clicks outside
    def enableOutputSetting(self):
        self.bitrateReductionSpinBox.setEnabled(True)
        self.bitrateReductionSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxEnableSS)
        self.fpsSpinBox.setEnabled(True)
        self.fpsSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxEnableSS)
        self.resolutionComboBox.setEnabled(True)
        self.resolutionComboBox.setStyleSheet(style_sheet.resolutionComboBoxEnableSS)

    def selectVidFile(self):
        self.fileName, status = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video File", r"",
                                                                      f"Video File({self.extensions})")
        if status:
            self.vidFile = os.path.normpath(self.fileName)
            self.enableAll()
            self.initVidObj()
            self.deleteThumbnail()

    def generateThumbnail(self):
        self.timeStp = self.generateTimeStamp()
        thumbnailDir = "images\\thumbnail\\"
        if not os.path.exists(thumbnailDir):
            os.makedirs(thumbnailDir)
        self.thumbnailPath = os.path.join(thumbnailDir, str(self.timeStp) + '.png')
        cmd = ['bin/ffmpeg', '-i', self.vidFile, '-ss', '00:00:01.000', '-vframes', '1', self.thumbnailPath]
        print(f'Thumbnail cmd: {cmd}')
        subprocess.run(cmd)
        self.infothumbnaiLabel.setPixmap(QPixmap(os.path.normpath(self.thumbnailPath)))

    @staticmethod
    def generateTimeStamp():
        dateTimeNow = datetime.now()
        return datetime.strftime(dateTimeNow, '%Y-%m-%d-%H-%M-%S')

    def deleteThumbnail(self):
        os.remove(self.thumbnailPath)

    def setOutputPath(self):
        currentDir = self.outputPathLineEdit.text()
        self.outputPathDirectory = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Output Folder")
        self.outputPathLineEdit.setText(self.outputPathDirectory)
        self.outputPathLineEdit.setToolTip(self.outputPathDirectory)
        if self.outputPathDirectory:
            self.modifiedAttributes['OUTPUTPATH'] = os.path.normpath(self.outputPathDirectory)
        else:
            self.outputPathLineEdit.setText(currentDir)
            self.outputPathLineEdit.setToolTip(self.outputPathDirectory)
            self.modifiedAttributes['OUTPUTPATH'] = currentDir

    def trimVideo(self):
        if not os.path.exists(self.vidFile):
            if self.messagebox:
                self.messagebox.close()
            self.messagebox = MessageBox('Error', 'Video File Is Missing.\n Make Sure Video File Exists.')
            self.messagebox.exec()
        else:
            if self.vPlayer:
                self.vPlayer.close()
            self.vPlayer = VideoPlayer(self)

    def play(self):
        if os.path.exists(self.vidFile):
            os.startfile(self.vidFile)
        else:
            if self.messagebox:
                self.messagebox.close()
            self.messagebox = MessageBox('Error', 'Video File Is Missing.\n Make Sure Video File Exists.')
            self.messagebox.exec()

    def updateMetaData(self):
        self.generateThumbnail()
        self.endTimeLineEdit.setPlaceholderText(self.vidFileObj.duration)
        self.infoNameLabel2.setText(os.path.basename(self.vidFile))
        self.infoNameLabel2.setToolTip(os.path.basename(self.vidFile))
        self.infoNameLabel2.setStyleSheet(style_sheet.infoAllLabel2EnableSS)
        self.infoSizeLabel2.setText(f'{str(self.vidFileObj.sizeMB)}MB')
        # self.minSize = int(self.vidFileObj.sizeMB * 0.40)
        self.minSize = self.vidFileObj.minimumPossibleSize
        self.provideSizeLineEdit.setPlaceholderText(f'Min Size => {int(self.minSize) + 1}')
        self.infoSizeLabel2.setStyleSheet(style_sheet.infoAllLabel2EnableSS)
        # self.infoLenghLabel2.setText(str(self.vidFileObj.duration))
        self.infoLenghLabel2.setText(str(self.vidFileObj.duration))
        self.infoLenghLabel2.setStyleSheet(style_sheet.infoAllLabel2EnableSS)
        self.infoBitrateLabel2.setText(str(self.vidFileObj.bitrate))
        self.infoBitrateLabel2.setStyleSheet(style_sheet.infoAllLabel2EnableSS)
        self.infoFpsLabel2.setText(str(self.vidFileObj.fps))
        self.infoFpsLabel2.setStyleSheet(style_sheet.infoAllLabel2EnableSS)
        self.infoResolutionLabel2.setText(str(self.vidFileObj.resolution))
        self.infoResolutionLabel2.setStyleSheet(style_sheet.infoAllLabel2EnableSS)

    def saveConfig(self):
        # Skipping Trimming Intervals if any
        self.modifiedAttributesCopy = self.modifiedAttributes.copy()
        try:
            del self.modifiedAttributesCopy['START']
            del self.modifiedAttributesCopy['END']
            del self.modifiedAttributesCopy['OUTPUTPATH']
        except KeyError:
            pass

        try:
            self.saveConfigFile, status = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Setting Profile', r"",
                                                                                'Pickle File(*.pickle)')
            if status:
                saveFileName = os.path.basename(self.saveConfigFile)
                with open(self.saveConfigFile, 'ab') as settingProfile:
                    print(f'Saving Setting Profile: {self.modifiedAttributesCopy}')
                    pickle.dump(self.modifiedAttributesCopy, settingProfile)
                if self.messagebox:
                    self.messagebox.close()
                self.messagebox = MessageBox('Success', f'Settings Profile {saveFileName} \nSaved Successfully!')
                self.messagebox.exec()
                # Update Counts
                self.countSaveConfig += 1
        except Exception as e:
            print(f'Could Not Save Settings Profile {self.saveConfigFile} \n "{e.args[-1]}"')
            if self.messagebox:
                self.messagebox.close()
            self.messagebox = MessageBox('Error', f'Could Not Save Settings Profile {saveFileName} \n "{e.args[-1]}"')
            self.messagebox.exec()

    def loadConfig(self):
        print('[DEBUG]: Loading Settings Profile')
        try:
            self.loadConfigFile, status = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Setting Profile', r"",
                                                                                'Pickle File(*.pickle)')
            if status:
                # Target Size Blocks Load Config Function, Hence, clearing the field
                self.provideSizeLineEdit.clear()
                loadFileName = os.path.basename(self.loadConfigFile)
                with open(self.loadConfigFile, 'rb') as settingsProfile:
                    self.modifiedAttributes = pickle.load(settingsProfile)
                    print(f'Loading Settings Profile: \n{self.modifiedAttributes}')
                    print(self.modifiedAttributes)
                if not self.modifiedAttributes['TARGETFILESIZEMB']:
                    if self.modifiedAttributes['BITRATE']:
                        self.bitrateReductionSpinBox.setValue(int(self.modifiedAttributes['BITRATE']))
                    else:
                        self.bitrateReductionSpinBox.setValue(5)
                    if self.modifiedAttributes['RESOLUTION']:
                        self.resolutionComboBox.setCurrentText(self.modifiedAttributes['RESOLUTION'])
                    else:
                        self.resolutionComboBox.setCurrentIndex(0)
                    if not self.modifiedAttributes['BITRATE'] and self.modifiedAttributes['FPS']:
                        self.fpsSpinBox.setValue(int(self.modifiedAttributes['FPS']))
                    elif not self.modifiedAttributes['FPS']:
                        self.fpsSpinBox.setValue(22)
                else:
                    self.provideSizeLineEdit.setText(self.modifiedAttributes['TARGETFILESIZEMB'])

                self.keepAudioCheckBox.setChecked(self.modifiedAttributes['AUDIO'])
                self.setFMT()
                # self.outputPathLineEdit.setText(self.modifiedAttributes['OUTPUTPATH'])
                # self.outputPathDirectory = self.outputPathLineEdit.text()
                self.updateSTART()
                self.updateEND()
                if self.messagebox:
                    self.messagebox.close()
                self.messagebox = MessageBox('Success', f'Settings Profile {loadFileName} \nLoaded Successfully!')
                self.messagebox.exec()
                # Update Count
                self.countLoadConfig += 1
        except Exception as e:
            print(f'[ERROR]: Could Not Load Settings Profile {loadFileName} \n"{e.args[-1]}"')
            if self.messagebox:
                self.messagebox.close()
            self.messagebox = MessageBox('Error',
                                         f'Could Not Load Settings Profile {self.loadConfigFile} \n"{e.args[-1]}"')
            self.messagebox.exec()

    def closeEvent(self, event):
        try:
            if self.worker.isRunning():
                self.interrupted = True
                self.killProcess('ffmpeg.exe')
                self.removeBrokenVidFile()
        except AttributeError:
            pass

        event.accept()

    @staticmethod
    def killProcess(processName):
        for proc in psutil.process_iter():
            if processName in proc.name():
                print(f'[Debug] Going to Kill {proc.name()} : {proc.pid}')
                proc.kill()

    def removeBrokenVidFile(self):
        fileToDelete = self.vidFileObj.outputFile
        while os.path.exists(fileToDelete):
            try:
                os.remove(fileToDelete)
                print(f'[Debug] Removed {fileToDelete}')
                time.sleep(1)
            except PermissionError:
                print('[WARNING] : Failed to delete the file, trying again.')
        print(f'Broken Video File {fileToDelete} Has Been Deleted!')

    def _close(self):
        self.close()
        if self.vPlayer:
            self.vPlayer.close()
        if self.messagebox:
            self.messagebox.close()

    def minimizeWindow(self):
        self.showMinimized()

    def openHelp(self):
        os.startfile(self.helpURL)

    def checkOutputFormat(self):
        if not os.path.exists(self.vidFile):
            if self.messagebox:
                self.messagebox.close()
            self.messagebox = MessageBox('Error', 'Video File Is Missing.\n Make Sure Video File Exists.')
            self.messagebox.exec()
        elif not any([
            self.mp4RadioButton.isChecked() or self.wmvRadioButton.isChecked() or self.aviRadioButton.isChecked()]):
            confirmFormat = OutputFormatMsgBox("Warning",
                                               "Your video will be converted to same format. \nDo you still want to proceed?")
            if press := confirmFormat.exec():
                self.startConversion()
            else:
                confirmFormat.close()
        else:
            self.startConversion()

    def startConversion(self):
        if self.vidFileObj.flagOK:
            self.mainFrame.setEnabled(False)
            self.disableAllButtonsStyle()
            self.worker = Worker(self.outputPathDirectory, self.modifiedAttributes, self.outputPathLineEdit,
                                 self.vidFileObj)
            self.worker.start()
            self.messagebox = MessageBox('Info', 'Conversion In-Progress!, You will be notified\n on completion!')
            self.messagebox.setEnabled(False)
            self.messagebox.buttonBox.clear()
            self.messagebox.show()
            self.worker.thread_finish.connect(self.finishThread)
        else:
            self.messagebox = MessageBox('Warn',
                                         'Conversion will not be continued, \n Since, Calculated Bitrate is too low.')

    def finishThread(self, msg):
        self.mainFrame.setEnabled(True)
        self.enableAllButtonsStyle()
        self.messagebox.close()
        if not self.interrupted:
            # self.updateCounts()
            print(f'OUTPUT DIR: {os.path.normpath(self.outputPathDirectory)}')
            os.startfile(os.path.normpath(self.outputPathDirectory))
            if self.messagebox:
                self.messagebox.close()
            self.messagebox = MessageBox('Success', msg)
            self.messagebox.exec()
            self.interrupted = False

        self.modifiedAttributes['TARGETFILESIZEMB'] = None

    # disable all when video is being converted
    def disableAllButtonsStyle(self):
        self.selectVideoButton.setStyleSheet(style_sheet.allPushButtonDisableSS)
        self.convertVideoButton.setStyleSheet(style_sheet.allPushButtonDisableSS)
        self.loadConfigButton.setStyleSheet(style_sheet.allPushButtonDisableSS)
        self.saveConfigButton.setStyleSheet(style_sheet.allPushButtonDisableSS)
        self.trimVideoButton.setStyleSheet(style_sheet.allPushButtonDisableSS)
        self.startTimeLineEdit.setStyleSheet(style_sheet.startEndTimeLineEditDisableSS)
        self.endTimeLineEdit.setStyleSheet(style_sheet.startEndTimeLineEditDisableSS)
        self.provideSizeLineEdit.setStyleSheet(style_sheet.provideSizeLineEditDisableSS)
        self.keepAudioCheckBox.setStyleSheet(style_sheet.keepAudioCheckBoxDisableSS)
        self.targetSizeLabel.setStyleSheet(style_sheet.infoAllLabel1DisableSS)
        self.bitrateReductionSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxDisableSS)
        self.fpsSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxDisableSS)
        self.resolutionComboBox.setStyleSheet(style_sheet.resolutionComboBoxDisableSS)
        self.infoplayVideoButton.setStyleSheet(style_sheet.infoplayVideoButtonDisableSS)

    def enableAllButtonsStyle(self):
        self.provideSizeLineEdit.clear()
        self.selectVideoButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.convertVideoButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.loadConfigButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.saveConfigButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.trimVideoButton.setStyleSheet(style_sheet.allPushButtonEnableSS)
        self.startTimeLineEdit.setStyleSheet(style_sheet.startEndTimeLineEditEnableSS)
        self.endTimeLineEdit.setStyleSheet(style_sheet.startEndTimeLineEditEnableSS)
        self.provideSizeLineEdit.setStyleSheet(style_sheet.provideSizeLineEditEnableSS)
        self.keepAudioCheckBox.setStyleSheet(style_sheet.keepAudioCheckBoxEnableSS)
        self.targetSizeLabel.setStyleSheet(style_sheet.infoAllLabel1SS)
        self.bitrateReductionSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxEnableSS)
        self.fpsSpinBox.setStyleSheet(style_sheet.bitrateReductionFpsSpinBoxEnableSS)
        self.resolutionComboBox.setStyleSheet(style_sheet.resolutionComboBoxEnableSS)
        self.infoplayVideoButton.setStyleSheet(style_sheet.infoplayVideoButtonEnableSS)


# Thread Class
class Worker(QThread):
    thread_finish = QtCore.Signal(str)

    def __init__(self, outputPathDirectory, modifiedAttributes, outputPathLineEdit, vidFileObj):
        super(Worker, self).__init__()
        self.outputPathDirectory = outputPathDirectory
        self.modifiedAttributes = modifiedAttributes
        self.outputPathLineEdit = outputPathLineEdit
        self.vidFileObj = vidFileObj

    def run(self):
        # Prepare Command
        self.outputPathDirectory = os.path.normpath(self.outputPathLineEdit.text())
        self.modifiedAttributes['OUTPUTPATH'] = self.outputPathDirectory
        print(f'MODIFIED_ATTRIBUTES: {self.modifiedAttributes}')
        cmd = self.vidFileObj.prepareCommand(**self.modifiedAttributes)
        print(f'\n{"~ " * len(cmd) * 4}\n')
        print(cmd)
        print(f'\n{"~ " * len(cmd) * 4}\n')

        # Run Command
        t1 = time.time()
        result = self.vidFileObj.runCommand(cmd)
        print(f'\n\n{result}')
        t2 = time.time()

        time_took = str(timedelta(seconds=t2 - t1)).split('.')[0]
        successMsg = f'Conversion Successful - Time Took: {time_took}'
        print(f'\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ [DEBUG] Time Took: {time_took} ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
        self.thread_finish.emit(successMsg)


if __name__ == '__main__':
    hide = ctypes.windll.kernel32.GetConsoleWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)
    app = QtWidgets.QApplication(sys.argv)
    dialog = videoController()
    dialog.setWindowOpacity(0.95)
    dialog.setWindowIcon(QIcon('icon.ico'))
    dialog.show()
    app.exec()
