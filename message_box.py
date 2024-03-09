import sys
import style_sheet

import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QFrame
from PySide6.QtGui import QPixmap, QIcon
import message_box_ui


class MessageBox(message_box_ui.Ui_Dialog, QtWidgets.QDialog, QtWidgets.QWidget):
    def __init__(self, messageType, message):
        super(MessageBox, self).__init__()
        self.dragPos = None
        self.messageType = messageType
        self.message = message
        self.setupUi(self)
        self.hideMenubar()
        self.messageBoxWindowLabel.setText(f"Video Player : {self.messageType}")

        # Mouse Move Event
        self.messageBoxMainFrame.mouseMoveEvent = self.moveWindow

        if messageType == "Warning":
            self.messageBoxTextLabel.setText(self.message)
            self.messageBoxTextIcon.setPixmap(QPixmap(u":/One/warn.ico"))
        elif messageType == "Error":
            self.messageBoxTextLabel.setText(self.message)
            self.messageBoxTextIcon.setPixmap(QPixmap(u":/One/cancel.ico"))
        elif messageType == "Info":
            self.animation()
            self.messageBoxTextLabel.setText(self.message)
            self.messageBoxTextIcon.setPixmap(QPixmap(u":/One/information.ico"))
        elif messageType == "Success":
            self.messageBoxTextLabel.setText(self.message)
            self.messageBoxTextIcon.setPixmap(QPixmap(u":/One/checked.ico"))

        # connections
        self.messageBoxCloseButton.clicked.connect(self.messageBoxClose)

        # Show MessageBox
        self.setWindowIcon(QIcon('icon.ico'))

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
        self.setWindowOpacity(0.95)

    def closeEvent(self, event):
        event.accept()

    def messageBoxClose(self):
        self.close()

    def animation(self):
        self.animationFrame = QtWidgets.QFrame(self.messageBoxMainFrame)
        self.animationFrame.setObjectName(u"animationFrame")
        self.animationFrame.setGeometry(QtCore.QRect(140, 130, 391, 21))
        self.animationFrame.setStyleSheet(style_sheet.animationFrameSS)
        self.animationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.animationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.animationFrame_2 = QtWidgets.QFrame(self.messageBoxMainFrame)
        self.animationFrame_2.setObjectName(u"animationFrame_2")
        self.animationFrame_2.setGeometry(QtCore.QRect(155, 145, 395, 21))
        self.animationFrame_2.setStyleSheet(style_sheet.animationFrame_2SS)
        self.animationFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.animationFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectFrame = QtWidgets.QFrame(self.animationFrame)
        self.rectFrame.setObjectName(u"rectFrame")
        self.rectFrame.setGeometry(QtCore.QRect(0, 0, 135, 21))
        self.rectFrame.setStyleSheet(style_sheet.rectFrameSS)
        self.rectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.amin = QtCore.QPropertyAnimation(self.animationFrame, b"geometry")
        self.amin.setLoopCount(200)
        self.amin.setDuration(3000)
        self.amin.setStartValue(QtCore.QRect(155, 145, 135, 21))
        self.amin.setEndValue(QtCore.QRect(415, 145, 135, 21))
        self.amin.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = MessageBox("Warning", "this is a info message")
    dialog.show()
    sys.exit(app.exec())
