from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys


class Pembeli(QMainWindow):
    def __init__(self):
        super().__init__()

        self.font = self.fontTemplate()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.leftSide())
        main_layout.addWidget(self.rightSide())
        main_layout.setStretch(0, 70)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def leftSide(self):
        self.stylesheet = """
        QWidget{
            font-family: 'Open Sans';
            color: #fff;
            background-color: #5f6caf;
        }
        QFrame{
            background-color: #5f6caf;
        }
        QPushButton{
            border: none;
            background-color: #5f6caf;
            font-size: 16px;
            font-weight: 500;
            padding: 24px;
        }
        QPushButton::hover, QPushButton::focus{
            color: #ffb677;
        }
        QPushButton::focus{
            background-color: #54609b;
        }
        QPushButton#logout{
            background-color: #ffb677;
            border: none;
            border-radius: 4;
            color: #333;
        }
        QPushButton#logout::hover{
            background-color: #ffa377;
        }

        QPushButton#logout:focus{
            background-color: #ff9066;
        }
        QLabel#title{
            font-family: 'Raleway';
            font-size: 32px;
            font-weight: bold;
        }
        QLabel#subtitle{
            font-size: 20px;
            fontweight: medium;
        }
        """

        # Buttons
        self.btnMakanan = QPushButton('Makanan', self)
        self.btnMakanan.setFont(self.font.textLabel)
        self.btnMinuman = QPushButton('Minuman', self)
        self.btnMinuman.setFont(self.font.textLabel)
        self.btnTransaksi = QPushButton('Transaksi', self)
        self.btnTransaksi.setFont(self.font.textLabel)
        # Widgets
        self.textNama = QLabel("Andisul")
        self.textNama.setFont(self.font.textTitle)
        self.textUang = QLabel("Rp. 2.000.000")
        self.textUang.setFont(self.font.textSubtitle)

        self.cmbPenjual = QComboBox()
        self.cmbPenjual.addItem("Lapak Nenek")
        self.cmbPenjual.addItem("Lapak Bude")

        self.frame = QFrame()
        self.frame.setLayoutDirection(Qt.LeftToRight)

        left_layout = QVBoxLayout(self.frame)
        left_layout.addWidget(self.textNama)
        left_layout.addWidget(self.textUang)
        left_layout.addWidget(self.cmbPenjual)
        left_layout.addStretch(1)
        left_layout.addWidget(self.btnMakanan)
        left_layout.addWidget(self.btnMinuman)
        left_layout.addWidget(self.btnTransaksi)
        left_layout.addStretch(1)

        left_widget = QWidget()
        left_widget.setStyleSheet(self.stylesheet)
        left_widget.setLayout(left_layout)
        return left_widget

    def rightSide(self):
        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; height: 0; margin: 0; padding: 0; border: none;}''')
        return self.right_widget

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
