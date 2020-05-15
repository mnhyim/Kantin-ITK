from PyQt5.QtWidgets import QWidget, QLabel


class PenjualWindow(QWidget):
    def __init__(self):
        super().__init__()
        lbl = QLabel("Penjual", self)
