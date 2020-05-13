#
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from src.Views.Login import Login

class MainWindow(QMainWindow):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        self.setWindowTitle("Kantin ITK")
        self.setGeometry(140,50,1100,650)
        self.setMinimumSize(1100, 650)
        self.setStyleSheet("background-color: #edf7fa")
        self.showMaximized()
        self.setWindowIcon(QIcon('../Assets/icon.png'))
        # Jadi yang perlu diubah buat ganti screen cukup dua line dibawah aja

        widget = Login()
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())