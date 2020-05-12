import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from src.Views.LoginLayout import LoginView, LoginViewLagi

class MainWindow(QMainWindow):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        self.setWindowTitle("Kantin ITK")
        self.showMaximized()

        label = QLabel("Main Window")
        label.setAlignment(Qt.AlignCenter)

        # Jadi yang perlu diubah buat ganti screen cukup dua line dibawah aja
        widget = LoginViewLagi()
        # widget = LoginView()
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
