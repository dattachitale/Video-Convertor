# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerldbjPX.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
                               QFrame, QLabel, QPushButton, QSizePolicy)
import icons
import style_sheet


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(676, 300)
        self.messageBoxMainFrame = QFrame(Dialog)
        self.messageBoxMainFrame.setObjectName(u"messageBoxMainFrame")
        self.messageBoxMainFrame.setGeometry(QRect(10, 10, 601, 231))
        self.messageBoxMainFrame.setStyleSheet(style_sheet.outputformatMessageBoxMainFrameSS)
        self.messageBoxMainFrame.setFrameShape(QFrame.StyledPanel)
        self.messageBoxMainFrame.setFrameShadow(QFrame.Raised)
        self.messageBoxTextIcon = QLabel(self.messageBoxMainFrame)
        self.messageBoxTextIcon.setObjectName(u"messageBoxTextIcon")
        self.messageBoxTextIcon.setGeometry(QRect(40, 88, 61, 61))
        self.messageBoxTextIcon.setStyleSheet(style_sheet.messageBoxTextIconSS)
        self.messageBoxTextIcon.setScaledContents(True)
        self.messageBoxTextLabel = QLabel(self.messageBoxMainFrame)
        self.messageBoxTextLabel.setObjectName(u"messageBoxTextLabel")
        self.messageBoxTextLabel.setGeometry(QRect(140, 60, 421, 91))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.messageBoxTextLabel.setFont(font)
        self.messageBoxTextLabel.setStyleSheet(style_sheet.messageBoxTextLabelSS)
        self.messageBoxWindowLabel = QLabel(self.messageBoxMainFrame)
        self.messageBoxWindowLabel.setObjectName(u"messageBoxWindowLabel")
        self.messageBoxWindowLabel.setGeometry(QRect(31, 0, 331, 61))
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(False)
        font1.setItalic(False)
        self.messageBoxWindowLabel.setFont(font1)
        self.messageBoxWindowLabel.setStyleSheet(style_sheet.messageBoxWindowLabelSS)
        self.messageBoxWindowLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.messageBoxCloseButton = QPushButton(self.messageBoxMainFrame)
        self.messageBoxCloseButton.setObjectName(u"messageBoxCloseButton")
        self.messageBoxCloseButton.setGeometry(QRect(524, 18, 41, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        # endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        # endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        # endif
        self.messageBoxCloseButton.setPalette(palette)
        font2 = QFont()
        font2.setPointSize(23)
        font2.setBold(True)
        self.messageBoxCloseButton.setFont(font2)
        self.messageBoxCloseButton.setStyleSheet(style_sheet.messageBoxCloseButtonSS)
        icon = QIcon()
        icon.addFile(u":/One/close.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.messageBoxCloseButton.setIcon(icon)
        self.messageBoxCloseButton.setIconSize(QSize(35, 35))
        self.messageBoxCloseButton.setAutoDefault(True)
        self.messageBoxCloseButton.setFlat(False)
        self.buttonBox = QDialogButtonBox(self.messageBoxMainFrame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(370, 161, 211, 61))
        self.buttonBox.setStyleSheet(style_sheet.buttonBoxSS)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No | QDialogButtonBox.Yes)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.messageBoxTextIcon.setText("")
        self.messageBoxTextLabel.setText(QCoreApplication.translate("Dialog", u" message type", None))
        self.messageBoxWindowLabel.setText(QCoreApplication.translate("Dialog", u"Video Player : ", None))
        self.messageBoxCloseButton.setText("")
    # retranslateUi
