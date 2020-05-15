from PyQt5.QtWidgets import QWidget, QLabel


class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        lbl = QLabel("Admin", self)
