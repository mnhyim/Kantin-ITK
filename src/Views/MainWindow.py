#
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from src.Views.LoginWindow import LoginWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        self.setWindowTitle("Kantin ITK")
        self.setStyleSheet("background-color: #edf7fa")
        self.showMaximized()
        self.setWindowIcon(QIcon('../Assets/icon.png'))

        self.setCentralWidget(LoginWindow())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
