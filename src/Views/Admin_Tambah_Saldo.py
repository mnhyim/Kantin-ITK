import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TambahSaldo(QWidget):
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
        QPushButton#tambahsaldo{
            background-color: #0314ff;
            border: none;
            border-radius: 4;
            color: #0a0807;
        }
        QPushButton#tambahsaldo::hover{
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

        self.chooseBuyer = QComboBox(self.centralWidget)
        self.chooseBuyer.addItems(['Andi', 'Gaple', 'Hacim', 'Habib'])
        self.chooseBuyer.setFixedHeight(35)
        self.chooseBuyer.setFont(font)

        font.setPointSize(20)
        self.totalLabel = QLabel("Jumlah Saldo     :", self.centralWidget)
        self.totalLabel.setFont(font)

        self.leditSaldo = QLineEdit(self.centralWidget)
        self.leditSaldo.setText("")
        self.leditSaldo.setFont(font)

        self.btnBack = QPushButton("Kembali", self.centralWidget)
        self.btnBack.setObjectName("back")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnAddsaldo = QPushButton("Tambah Saldo", self.centralWidget)
        self.btnAddsaldo.setObjectName("tambahsaldo")
        self.btnAddsaldo.setFixedSize(200, 40)
        self.btnAddsaldo.setFont(font)
        self.btnAddsaldo.setCursor(QCursor(Qt.PointingHandCursor))

        layoutHor1 = QHBoxLayout()
        layoutHor1.addWidget(self.chooseBuyer)

        layoutHor2 = QHBoxLayout()
        layoutHor2.addWidget(self.totalLabel)
        layoutHor2.addWidget(self.leditSaldo)

        layoutHor3 = QHBoxLayout()
        layoutHor3.addWidget(self.btnAddsaldo, alignment=Qt.AlignCenter)

        layoutBack = QHBoxLayout()
        layoutBack.addWidget(self.btnBack, alignment=Qt.AlignLeft)

        vertical = QVBoxLayout(self.centralWidget)
        vertical.addLayout(layoutBack)
        vertical.addStretch()
        vertical.addLayout(layoutHor1)
        vertical.addLayout(layoutHor2)
        for i in range(20):
            vertical.addStretch()
        vertical.addLayout(layoutHor3)

        self.centralWidget.setLayout(vertical)
