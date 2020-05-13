import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TambahSaldo(QMainWindow):
    def __init__(self):
        super(TambahSaldo, self).__init__()

        # self.sidebarUI()
        self.rightSide()
        # self.createHorizontalLayout()

    def rightSide(self):
        self.stylesheet = """
        QWidget{
            font-family: 'Open Sans';
            color: #030303;
        }
        QPushButton{
            font-size: 16px;
            font-weight: 500;
            border-radius : 4;
        }
        QPushButton#back{
            background-color: #e0dad2;
            border: none;
            color: #0a0807;
        }
        QPushButton#tambahmenu{
            background-color: #0314ff;
            border: none;
            border-radius: 4;
            color: #0a0807;
        }
        QPushButton#tambahmenu::hover{
            background-color: #0c1b7d;
        }
        
        """

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("mainbar")
        self.centralWidget.move(400, 0)
        self.centralWidget.setStyleSheet(self.stylesheet)
        self.centralWidget.setFixedSize(720, 720)

        font = QFont("Arial")
        font.setPointSize(15)
        font.setWordSpacing(0)

        font.setPointSize(20)
        self.titlemenu = QLabel("Tambah Menu", self.centralWidget)
        self.titlemenu.setFont(font)


        font.setPointSize(20)
        self.namamenu = QLabel("Nama Menu :", self.centralWidget)
        self.namamenu.setFont(font)

        self.lmenu = QLineEdit(self.centralWidget)
        self.lmenu.setText("")
        self.lmenu.setFont(font)

        font.setPointSize(20)
        self.harga = QLabel("Harga Menu :", self.centralWidget)
        self.harga.setFont(font)

        self.ltambahmenu = QLineEdit(self.centralWidget)
        self.ltambahmenu.setText("")
        self.ltambahmenu.setFont(font)

        self.btnBack = QPushButton("Kembali", self.centralWidget)
        self.btnBack.setObjectName("back")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnAddsaldo = QPushButton("Tambah Menu", self.centralWidget)
        self.btnAddsaldo.setObjectName("tambahmenu")
        self.btnAddsaldo.setFixedSize(200, 40)
        self.btnAddsaldo.setFont(font)
        self.btnAddsaldo.setCursor(QCursor(Qt.PointingHandCursor))

        layoutHortitle = QHBoxLayout()
        layoutHortitle.addWidget(self.titlemenu)

        layoutHor1 = QHBoxLayout()
        layoutHor1.addWidget(self.namamenu)
        layoutHor1.addWidget(self.lmenu)

        layoutHor2 = QHBoxLayout()
        layoutHor2.addWidget(self.harga)
        layoutHor2.addWidget(self.ltambahmenu)

        layoutHor3 = QHBoxLayout()
        layoutHor3.addWidget(self.btnAddsaldo, alignment=Qt.AlignCenter)

        layoutBack = QHBoxLayout()
        layoutBack.addWidget(self.btnBack, alignment=Qt.AlignLeft)

        vertical = QVBoxLayout(self.centralWidget)
        vertical.addLayout(layoutBack)
        vertical.addStretch()
        vertical.addLayout(layoutHortitle)
        vertical.addLayout(layoutHor1)
        vertical.addLayout(layoutHor2)
        for i in range(20):
            vertical.addStretch()
        vertical.addLayout(layoutHor3)

        self.centralWidget.setLayout(vertical)
