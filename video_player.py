from datetime import timedelta
from PySide6 import QtMultimedia, QtMultimediaWidgets
import sys
import PySide6.QtWidgets as QtWidgets
import PySide6.QtCore as QtCore
from PySide6.QtMultimedia import QMediaPlayer
import video_player_ui
import style_sheet
from message_box import MessageBox

class VideoPlayer(video_player_ui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, vidObject, parent=None):
        super(VideoPlayer, self).__init__(parent=parent)
        self.dragPos = None
        self.startPosSec = 0
        self.endPosSec = 0
        self.endPos = None
        self.startPos = None
        self.vidObject = vidObject
        self.setupUi(self)

        self.videoPlayerWidget = QtMultimediaWidgets.QVideoWidget(self.centralwidget)
        self.videoPlayerWidget.setGeometry(QtCore.QRect(33, 93, 826, 376))
        self.videoPlayerWidget.setPalette(QtCore.Qt.black)

        self.audioOutput = QtMultimedia.QAudioOutput()
        self.mediaPlayer = QtMultimedia.QMediaPlayer()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setVideoOutput(self.videoPlayerWidget)

        self.mediaPlayer.setSource(QtCore.QUrl.fromLocalFile(self.vidObject.vidFileObj.inputPath))
        self.playVideo()
        self.playButton.setEnabled(False)

        # connections
        self.playButton.clicked.connect(self.playVideo)
        self.pauseButton.clicked.connect(self.pauseVideo)
        self.stopButton.clicked.connect(self.stopVideo)
        self.mediaPlayer.positionChanged.connect(self.pos_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.seekSlider.sliderMoved.connect(self.set_Position)
        self.startTrimButton.clicked.connect(self.recordStartTrim)
        self.endTrimButton.clicked.connect(self.recordEndTrim)
        self.confirmSettingsButton.clicked.connect(self.confirmSettings)
        self.discardSettingsButton.clicked.connect(self.discardSettings)
        self.resetSettingsButton.clicked.connect(self.resetSettings)
        self.hideMenubar()
        self.show()

        # Mouse Move Event
        self.trimMainFrame.mouseMoveEvent = self.moveWindow
        self.trimWindowLabel.mouseMoveEvent = self.moveWindow
        self.videoPlayerWidget.mouseMoveEvent = self.moveWindow

        # Resetting endTrimLabel
        self.endTrimLabel.setText(self.vidObject.vidFileObj.duration)

    def hideMenubar(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def moveWindow(self, event):
        try:
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                event.accept()
                self.dragPos = event.globalPosition().toPoint()
        except TypeError:
            pass

    def playVideo(self):
        self.mediaPlayer.play()
        self.playButton.setEnabled(False)
        self.playButton.setStyleSheet(style_sheet.playButtonDisableSS)
        self.stopButton.setEnabled(True)
        self.stopButton.setStyleSheet(style_sheet.stopButtonEnableSS)
        self.pauseButton.setEnabled(True)
        self.pauseButton.setStyleSheet(style_sheet.pauseButtonEnableSS)

    def pauseVideo(self):
        self.mediaPlayer.pause()
        self.pauseButton.setEnabled(False)
        self.pauseButton.setStyleSheet(style_sheet.pauseButtonDisableSS)
        self.playButton.setEnabled(True)
        self.playButton.setStyleSheet(style_sheet.playButtonEnableSS)
        self.stopButton.setEnabled(True)
        self.stopButton.setStyleSheet(style_sheet.stopButtonEnableSS)

    def stopVideo(self):
        self.mediaPlayer.stop()
        self.mediaPlayer.setPosition(0)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setStyleSheet(style_sheet.pauseButtonDisableSS)
        self.playButton.setEnabled(True)
        self.playButton.setStyleSheet(style_sheet.playButtonEnableSS)
        self.stopButton.setEnabled(False)
        self.stopButton.setStyleSheet(style_sheet.stopButtonDisableSS)

    def pos_changed(self, position):
        self.seekSlider.setValue(position)
        self.videoDurationLabel.setText(str(timedelta(seconds=position / 1000)).split(".")[0])

    def duration_changed(self, duration):
        self.seekSlider.setRange(0, duration)

    def set_Position(self, position):
        self.mediaPlayer.setPosition(position)

    def recordStartTrim(self):
        self.pauseVideo()
        self.startPosSec = self.mediaPlayer.position() / 1000
        print(self.startPosSec)
        self.startPos = timedelta(seconds=self.startPosSec)
        self.startPos = str(self.startPos).split('.')[0]
        print(f'START: {self.startPos}')
        self.startTrimLabel.setText(str(self.startPos))

    def recordEndTrim(self):
        self.pauseVideo()
        self.endPosSec = self.mediaPlayer.position() / 1000
        print(self.endPosSec)
        self.endPos = timedelta(seconds=self.endPosSec)
        self.endPos = str(self.endPos).split('.')[0]
        print(f'END: {self.endPos}')
        self.endTrimLabel.setText(str(self.endPos))

    def closeEvent(self, event):
        self.forceStop()
        event.accept()

    def confirmSettings(self):
        diff = 0
        _start = '00:00:00' if not self.startPos else self.startPos
        _end = self.vidObject.vidFileObj.duration if not self.endPos else self.endPos

        _startPosSec = 0 if not self.startPosSec else self.startPosSec
        _endPosSec   = int(self.mediaPlayer.duration()/1000) if not self.endPosSec else self.endPosSec

        self.vidObject.provideSizeLineEdit.clear()

        if self.endPosSec or self.startPosSec:
            diff = int(_endPosSec) - int(_startPosSec)
            print(f'DIFF: {diff} Seconds')

            if abs(diff) >= 5:
                if diff <= -5:
                    _start, _end = _end, _start
                    self.vidObject.startTimeLineEdit.setText(self.endTrimLabel.text())
                    self.vidObject.endTimeLineEdit.setText(self.startTrimLabel.text())
                    diff *= -1
                else:
                    self.vidObject.startTimeLineEdit.setText(self.startTrimLabel.text())
                    self.vidObject.endTimeLineEdit.setText(self.endTrimLabel.text())

                # Re-calculate the minimum size for Target Size Feature
                self.vidObject.minSize = int((diff * self.vidObject.vidFileObj.bitrateNum * self.vidObject.vidFileObj.bitRateReductionFactor) / (1024 * 8))
                print(f'Updated Minimum Size: {self.vidObject.minSize} MB')
                self.vidObject.provideSizeLineEdit.setPlaceholderText(f'Min Size => {int(self.vidObject.minSize) + 1}')
            else:
                print('Please provide minimum trimming interval of 5 seconds.')
                msgBox = MessageBox('Warning', 'Please provide minimum trimming \ninterval of 5 seconds.')
                msgBox.exec()
        else:
            self.vidObject.startTimeLineEdit.setText('00:00:00')
            self.vidObject.endTimeLineEdit.setText(str(self.vidObject.vidFileObj.duration))

        if not diff:
            self.pauseVideo()
            msgBox = MessageBox('Warning', 'No Time Interval Provided \nPlease provide 5 sec minimum interval OR '
                                           '\n Use Discard to Exit')
            msgBox.exec()
            # self.close()
        elif abs(diff) >= 5:
            self.close()

    def resetSettings(self):
        # Reset TrimLabels on VPlayer
        self.startTrimLabel.setText('00:00:00')
        self.startPosSec = None
        self.endTrimLabel.setText(str(self.vidObject.vidFileObj.duration))
        self.endPosSec = None
        self.vidObject.minSize = self.vidObject.vidFileObj.minimumPossibleSize
        self.vidObject.provideSizeLineEdit.setPlaceholderText(f'Min Size => {int(self.vidObject.vidFileObj.minimumPossibleSize) + 1}')
        self.stopVideo()

    def discardSettings(self):
        self.close()

    def forceStop(self):
        if self.mediaPlayer.playbackState() != QMediaPlayer.StoppedState:
            self.stopVideo()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = VideoPlayer('Media player')
    dialog.show()
    sys.exit(app.exec())
