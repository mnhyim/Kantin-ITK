from PyQt5.QtWidgets import QWidget, QLabel


class PembeliWindow(QWidget):
    def __init__(self):
        super().__init__()
        lbl = QLabel("Pembeli", self)
