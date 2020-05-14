from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from Pembeli_Minuman import PembeliMinuman

class Pembeli(QMainWindow):
    def __init__(self):
        super(Pembeli, self).__init__()

        self.font = self.fontTemplate()

        self.tab1 = self.makananUi()
        self.tab2 = self.minumanUi()
        self.tab3 = self.transaksiUi()

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
        QComboBox{
            background-color: #fff;
            color: #333;
            border: none;
            border-radius: 4;
        }
        """

        # Buttons
        self.btnMakanan = QPushButton('Makanan', self)
        self.btnMakanan.setFont(self.font.textLabel)
        self.btnMakanan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMakanan.clicked.connect(self.button1)

        self.btnMinuman = QPushButton('Minuman', self)
        self.btnMinuman.setFont(self.font.textLabel)
        self.btnMinuman.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMinuman.clicked.connect(self.button2)

        self.btnTransaksi = QPushButton('Transaksi', self)
        self.btnTransaksi.setFont(self.font.textLabel)
        self.btnTransaksi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnTransaksi.clicked.connect(self.button3)

        self.btnLogout = QPushButton('Logout', self)
        self.btnLogout.setObjectName("logout")
        self.btnLogout.setFont(self.font.textLabel)
        self.btnLogout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogout.clicked.connect(self.buttonLogout)
        # Widgets
        self.textNama = QLabel("Andisul")
        self.textNama.setFont(self.font.textTitle)
        self.textUang = QLabel("Rp. 2.000.000")
        self.textUang.setFont(self.font.textSubtitle)

        self.cmbPenjual = QComboBox()
        self.cmbPenjual.addItem("Lapak Nenek")
        self.cmbPenjual.addItem("Lapak Bude")
        self.cmbPenjual.setFixedHeight(35)
        
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
        left_layout.addWidget(self.btnLogout)
        left_layout.addStretch(0)

        left_widget = QWidget()
        left_widget.setStyleSheet(self.stylesheet)
        left_widget.setLayout(left_layout)
        return left_widget

    def rightSide(self):
        self.style = """
        QTabBar::tab{
            width: 0;
            height: 0;
            margin: 0;
            padding: 0;
            border: none;
        }
        """
        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet(self.style)

        return self.right_widget

    def button1(self):
        self.right_widget.setCurrentIndex(0)
    
    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def buttonLogout(self):
        from Login import Login

        self.back = Login()
        self.parent().setCentralWidget(self.back)

    def makananUi(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('PAGE MAKANAN'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def minumanUi(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('PAGE MINUMAN'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def transaksiUi(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('PAGE TRANSAKSI'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


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
