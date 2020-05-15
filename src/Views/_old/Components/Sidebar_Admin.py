import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class SidebarAdmin(QWidget):
    def __init__(self):
        super(SidebarAdmin, self).__init__()

        self.sidebarUI()

    def sidebarUI(self):
        self.stylesheet = """
        QWidget{
            font-family: 'Open Sans';
            color: #fff;
        }
        QFrame{
            background-color: #5f6caf;
        }
        QPushButton{
            border: none;
            background-color: #5f6caf;
            font-size: 16px;
            font-weight: 500;

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
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("sidebar")
        self.centralWidget.setFixedSize(420,720)
        self.centralWidget.setStyleSheet(self.stylesheet)

        self.frame = QFrame(self.centralWidget)
        self.frame.setFixedSize(300, 720)
        self.frame.setLayoutDirection(Qt.LeftToRight)

        self.title = QLabel("Kantin ITK", self.frame)
        self.title.setObjectName("title")
        self.title.setGeometry(15, 10, 200, 50)

        self.subtitle = QLabel("Andi Sultan", self.frame)
        self.subtitle.setObjectName("subtitle")
        self.subtitle.setGeometry(15, 60, 250, 50)
        self.subtitle.setScaledContents(True)
        self.subtitle.setAlignment(Qt.AlignLeft)
        self.subtitle.setWordWrap(True)

        self.btnAdmin = QPushButton("Admin", self.frame)
        self.btnAdmin.setGeometry(0,200, 300, 80)
        self.btnAdmin.setObjectName("admin")
        self.btnAdmin.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnPembeli = QPushButton("Pembeli", self.frame)
        self.btnPembeli.setGeometry(0, 280, 300, 80)
        self.btnPembeli.setObjectName("pembeli")
        self.btnPembeli.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnPenjual = QPushButton("Penjual", self.frame)
        self.btnPenjual.setGeometry(0, 360, 300, 80)
        self.btnPenjual.setObjectName("penjual")
        self.btnPenjual.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnTambahsaldo = QPushButton("Tambah Saldo", self.frame)
        self.btnTambahsaldo.setGeometry(0, 440, 300, 80)
        self.btnTambahsaldo.setObjectName("tambahsaldo")
        self.btnTambahsaldo.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnLogout = QPushButton("Logout", self.frame)
        self.btnLogout.setGeometry(60,600, 180, 45)
        self.btnLogout.setObjectName("logout")
        self.btnLogout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogout.clicked.connect(self.logout)

    def logout(self):
        from Login import Login
        self.back = Login()
        self.parent().setCentralWidget(self.back)



