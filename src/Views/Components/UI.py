from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton


class Stylesheet():
    def __init__(self):
        self.stylesheet = """
            QFrame{
                background-color: #39538D;
                color: #eee;
            }
        """


class FontTemplate():
    def fontTemplate(self):
        self.textTitle = QFont()
        self.textTitle.setPointSize(24)
        self.textTitle.setWeight(65)

        self.textSubtitle = QFont()
        self.textSubtitle.setPointSize(12)
        self.textSubtitle.setWeight(50)

        self.textLabel = QFont()
        self.textLabel.setPointSize(12)
        self.textLabel.setWeight(65)

        self.textPlaceholder = QFont()
        self.textPlaceholder.setPointSize(10)
        self.textPlaceholder.setWeight(20)

        return self


class FrameTemplate:
    def __init__(self):
        pass


class customPushButton(QPushButton):
    def __init__(self, isi, tipe="", parent=None):
        super().__init__(parent)
        self.styleSheet = """
            QPushButton{
                font-size: 14px;
                font-weight: 500;
                border-radius : 2;
                padding: 2px 6px;
            }
            
            QPushButton#primary{
                background-color: #243E79;
                color: #eee;
            }
            QPushButton#primary:hover{
                background-color: #566EA4;
                color: #eee;
            }
            QPushButton#primary:pressed{
                background-color:#273961;
                color: #eee;
            }
            
            QPushButton#secondary{
                background-color: #f28b38;
                color: #eee;
            }
            QPushButton#secondary:hover{
                background-color: #ff943d;
                color: #eee;
            }
            QPushButton#secondary:pressed{
                background-color: #e08234;
                color: #eee;
            }
            """
        self.setText(isi)
        self.setObjectName(tipe)
        self.setStyleSheet(self.styleSheet)
        # self.clicked.connect(act)
