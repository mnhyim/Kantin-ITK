import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class EditMenu(QWidget):
    def __init__(self):
        super(EditMenu, self).__init__()

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
        QPushButton#edit{
            background-color: #0314ff;
            border: none;
            border-radius: 4;
            color: #0a0807;
        }
        QPushButton#edit::hover{
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
        self.nama = QLabel("Edit Menu     :", self.centralWidget)
        self.nama.setFont(font)
    #combo box menu
        self.chooseBuyer = QComboBox(self.centralWidget)
        self.chooseBuyer.addItems(['Nasi Goreng','Ayam Geprek' , 'Es Jeruk', 'Es Teh'])
        self.chooseBuyer.setFixedHeight(35)
        self.chooseBuyer.setFont(font)

    #harga baru
        self.harga = QLabel("Harga Baru     :", self.centralWidget)
        self.harga.setFont(font)

        self.leditharga = QLineEdit(self.centralWidget)
        self.leditharga.setText("")
        self.leditharga.setFont(font)

        self.btnBack = QPushButton("Kembali", self.centralWidget)
        self.btnBack.setObjectName("back")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnedit = QPushButton("Edit", self.centralWidget)
        self.btnedit.setObjectName("edit")
        self.btnedit.setFixedSize(200, 40)
        self.btnedit.setFont(font)
        self.btnedit.setCursor(QCursor(Qt.PointingHandCursor))

        layoutHor0 = QHBoxLayout()
        layoutHor0.addWidget(self.nama)

        layoutHor1 = QHBoxLayout()
        layoutHor1.addWidget(self.chooseBuyer)

        layoutHor2 = QHBoxLayout()
        layoutHor2.addWidget(self.harga)
        layoutHor2.addWidget(self.leditharga)

        layoutHor3 = QHBoxLayout()
        layoutHor3.addWidget(self.btnedit, alignment=Qt.AlignCenter)

        layoutBack = QHBoxLayout()
        layoutBack.addWidget(self.btnBack, alignment=Qt.AlignLeft)

        vertical = QVBoxLayout(self.centralWidget)
        vertical.addLayout(layoutBack)
        vertical.addStretch()
        vertical.addLayout(layoutHor0)
        vertical.addLayout(layoutHor1)
        vertical.addLayout(layoutHor2)
        for i in range(20):
            vertical.addStretch()
        vertical.addLayout(layoutHor3)

        self.centralWidget.setLayout(vertical)
