import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# from src.Class.Penjual import Penjual


class TambahMenu(QMainWindow):
    def __init__(self):
        super(TambahMenu, self).__init__()

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
        # self.centralWidget.move(400, 0)
        self.centralWidget.setStyleSheet(self.stylesheet)
        self.centralWidget.setFixedSize(720, 720)

        font = QFont("Arial")
        font.setPointSize(15)
        font.setWordSpacing(0)

        font.setPointSize(20)
        self.titlemenu = QLabel("Tambah Menu", self.centralWidget)
        self.titlemenu.setFont(font)

    #nama
        self.namamenu = QLabel("Nama Menu :", self.centralWidget)
        self.namamenu.setFont(font)

        self.lmenu = QLineEdit(self.centralWidget)
        self.lmenu.setText("")
        self.lmenu.setFont(font)

    #type
        self.edit = QLabel("Type Menu   :", self.centralWidget)
        self.edit.setFont(font)

        self.chooseBuyer = QComboBox(self.centralWidget)
        self.chooseBuyer.addItems(['Titipan','Biasa'])
        self.chooseBuyer.setFixedHeight(35)
        self.chooseBuyer.setFont(font)
    #merk
        self.merkmenu = QLabel("Merk Menu   :", self.centralWidget)
        self.merkmenu.setFont(font)

        self.lmerk = QLineEdit(self.centralWidget)
        self.lmerk.setText("")
        self.lmerk.setFont(font)

    #harga
        self.harga = QLabel("Harga Menu :", self.centralWidget)
        self.harga.setFont(font)

        self.ltambahmenu = QLineEdit(self.centralWidget)
        self.ltambahmenu.setText("")
        self.ltambahmenu.setFont(font)

    #kuantitas
        self.kuantitas = QLabel("Kuantitas     :", self.centralWidget)
        self.kuantitas.setFont(font)

        self.lkuantitas = QLineEdit(self.centralWidget)
        self.lkuantitas.setText("")
        self.lkuantitas.setFont(font)

    #btnkembali
        self.btnBack = QPushButton("Kembali", self.centralWidget)
        self.btnBack.setObjectName("back")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))
    #btntambah
        self.btnAddmenu = QPushButton("Tambah Menu", self.centralWidget)
        self.btnAddmenu.setObjectName("tambahmenu")
        self.btnAddmenu.setFixedSize(200, 40)
        self.btnAddmenu.setFont(font)
        self.btnAddmenu.setCursor(QCursor(Qt.PointingHandCursor))

        layoutHortitle = QHBoxLayout()
        layoutHortitle.addWidget(self.titlemenu)

        layoutHornama = QHBoxLayout()
        layoutHornama.addWidget(self.namamenu)
        layoutHornama.addWidget(self.lmenu)

        layoutHortipe = QHBoxLayout()
        layoutHortipe.addWidget(self.edit)
        layoutHortipe.addWidget(self.chooseBuyer)

        layoutHorharga = QHBoxLayout()
        layoutHorharga.addWidget(self.harga)
        layoutHorharga.addWidget(self.ltambahmenu)

        layoutHormerk = QHBoxLayout()
        layoutHormerk.addWidget(self.merkmenu)
        layoutHormerk.addWidget(self.lmerk)

        layoutHorkuantitas = QHBoxLayout()
        layoutHorkuantitas.addWidget(self.kuantitas)
        layoutHorkuantitas.addWidget(self.lkuantitas)

        layoutHor3 = QHBoxLayout()
        layoutHor3.addWidget(self.btnAddmenu, alignment=Qt.AlignCenter)

        layoutBack = QHBoxLayout()
        layoutBack.addWidget(self.btnBack, alignment=Qt.AlignLeft)

        vertical = QVBoxLayout(self.centralWidget)
        vertical.addLayout(layoutBack)
        vertical.addStretch()
        vertical.addLayout(layoutHortitle)
        vertical.addLayout(layoutHornama)
        vertical.addLayout(layoutHortipe)
        vertical.addLayout(layoutHormerk)
        vertical.addLayout(layoutHorharga)
        vertical.addLayout(layoutHorkuantitas)
        for i in range(20):
            vertical.addStretch()
        vertical.addLayout(layoutHor3)

        self.centralWidget.setLayout(vertical)
