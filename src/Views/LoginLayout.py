import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout


class LoginView(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Login")

        vLayoutKiri = QVBoxLayout()
        vLayoutKiri.addWidget(Color('red'))
        vLayoutKiri.addWidget(QLabel("kiri"))
        vLayoutKiri.addWidget(QLabel("kiri"))

        vLayoutKanan = QVBoxLayout()
        vLayoutKanan.addWidget(QLabel("Kanan"))
        vLayoutKanan.addWidget(QLabel("Kanan"))
        vLayoutKanan.addWidget(QLabel("Kanan"))
        vLayoutKanan.addWidget(QLabel("Kanan"))

        hLayout = QHBoxLayout()
        hLayout.addLayout(vLayoutKiri)
        hLayout.addLayout(vLayoutKanan)

        self.setLayout(hLayout)
