from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

from src.Views.Components.UI import customPushButton, Stylesheet


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        x = Stylesheet()
        self.setStyleSheet(x.stylesheet)
        hLayout = QHBoxLayout()
        hLayout.addWidget(Left())
        hLayout.addWidget(Right())
        hLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hLayout)


class Left(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("A", self)
        customPushButton(isi="Primary", tipe="primary", parent=self)


class Right(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("AS", self)
