import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout


class LoginView(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Login")

        label = QLabel("Habib cupu")
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")

        Vlayout = QVBoxLayout()
        Vlayout.addWidget(label)
        Vlayout.addWidget(label1)
        Vlayout.addWidget(label2)
        Vlayout.addWidget(label3)

        self.setLayout(Vlayout)


class LoginViewLagi(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Login")

        label = QLabel("Gaplek cupu")
        label1 = QLabel("Label 5")
        label2 = QLabel("Label 6")
        label3 = QLabel("Label 7")

        Vlayout = QHBoxLayout()
        Vlayout.addWidget(label)
        Vlayout.addWidget(label1)
        Vlayout.addWidget(label2)
        Vlayout.addWidget(label3)

        self.setLayout(Vlayout)
