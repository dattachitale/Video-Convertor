import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap, QIcon

from PySide6 import QtCore
import output_format_msgbox_UI
import sys


class OutputFormatMsgBox(output_format_msgbox_UI.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self,messageType, message):
        super(OutputFormatMsgBox, self).__init__()
        self.messageType = messageType
        self.message = message
        self.setupUi(self)
        self.hideMenubar()
        self.messageBoxWindowLabel.setText(f"Video Player : {self.messageType}")
        # self.buttonBox.clear()

        self.messageBoxTextLabel.setText(self.message)
        self.messageBoxTextIcon.setPixmap(QPixmap(u":/One/warn.ico"))

        # Mouse Move Event
        self.messageBoxMainFrame.mouseMoveEvent = self.moveWindow

        # connections
        self.messageBoxCloseButton.clicked.connect(self.messageBoxClose)

        # Show MessageBox
        self.setWindowIcon(QIcon('icon.ico'))
        # self.showMaximized()
        # self.show()
        # self.exec()

    def hideMenubar(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.95)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def moveWindow(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            event.accept()
            self.dragPos = event.globalPosition().toPoint()

    def closeEvent(self, event):
        event.accept()

    def messageBoxClose(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = OutputFormatMsgBox("Warning", "this is a info message")
    dialog.show()
    sys.exit(app.exec())
