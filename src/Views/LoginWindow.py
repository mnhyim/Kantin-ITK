from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QFrame

from src.Views.Components.UI import customPushButton, Stylesheet


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        x = Stylesheet()
        self.setStyleSheet(x.stylesheet)
        hLayout = QHBoxLayout()
        hLayout.addWidget(Left(), 1)
        hLayout.addWidget(Right(), 3)
        hLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hLayout)


class Left(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            """
                QFrame{
                    background-color: #000;
                }
            """
        )

        self.bgFrame = QFrame()
        self.bgFrame.setObjectName("bgFrame")

        a = customPushButton(isi="Primary", tipe="primary", parent=self)
        b = customPushButton(isi="Primary", tipe="secondary", parent=self)

        self.vLayout = QVBoxLayout(self.bgFrame)
        self.vLayout.addWidget(a)
        self.vLayout.addWidget(b)

        self.setLayout(self.vLayout)


class Right(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("right", self)
