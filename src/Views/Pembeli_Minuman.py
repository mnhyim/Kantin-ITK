import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from adminlihatpenjual import LihatPenjual

class MenuMinuman(QWidget):
    def __init__(self):
        super(MenuMinuman, self).__init__()
        
       # self.sidebarUI()
        self.rightSide()
        #self.createHorizontalLayout()
        

    def rightSide(self):
        self.stylesheet = """
        QWidget{
            font-family: 'Open Sans';
            color: #030303;
        }
        QGroupBox{
            border : 4px solid #201a9c;
        }

        QPushButton{
            border : none;
            background-color : #454545;
            color : white;
        }
        QPushButton#tambah{
            background-color: #dbd9d8;
            border: none;
            color: #0a0807;
        }
        QPushButton#tambah::hover{
            background-color: #c2bebb;
        }
        QPushButton#edit{
            background-color: #dbd9d8;
            border: none;
            color: #0a0807;
        }
        QPushButton#edit::hover{
            background-color: #c2bebb;
        }

        
        """

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("mainbar")
        self.centralWidget.move(200, 0)
        self.centralWidget.setStyleSheet(self.stylesheet)
        self.centralWidget.setFixedSize(720, 720)

        
        font = QFont("Arial") 
        font.setPointSize(30)
        font.setWordSpacing(0)
        font.setBold(4)

        self.labelMenu = QLabel("Menu", self.centralWidget)
        self.labelMenu.setFont(font)
        self.labelMenu.adjustSize()
        self.labelMenu.move(610,30)
        
        grid = QGridLayout(self.centralWidget)

        self.group1 = QGroupBox()
        self.group2 = QGroupBox()
        self.group3 = QGroupBox()
        self.group4 = QGroupBox()
        self.group5 = QGroupBox()
        self.group6 = QGroupBox()
        self.group7 = QGroupBox()
        self.group8 = QGroupBox()
        
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        vbox4 = QVBoxLayout()
        vbox5 = QVBoxLayout()
        vbox6 = QVBoxLayout()
        vbox7 = QVBoxLayout()
        vbox8 = QVBoxLayout()
        
        self.labelPesan = QLabel("Es Teh Panas", self.centralWidget)
        self.btnPesan = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan.setMinimumHeight(20)
        self.btnPesan.setCursor(QCursor(Qt.PointingHandCursor))
        vbox1.addStretch(3)
        vbox1.addWidget(self.labelPesan)
        vbox1.addWidget(self.btnPesan)
        self.group1.setLayout(vbox1)
        self.group1.setMaximumHeight(150)


        self.labelPesan1 = QLabel("Es Teh Panas", self.centralWidget)
        self.btnPesan1 = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan1.setMinimumHeight(20)
        self.btnPesan1.setCursor(QCursor(Qt.PointingHandCursor))
        vbox2.addStretch(3)
        vbox2.addWidget(self.labelPesan1)
        vbox2.addWidget(self.btnPesan1)
        self.group2.setLayout(vbox2)
        self.group2.setMaximumHeight(150)

        self.labelPesan2 = QLabel("Es Teh Panas", self.centralWidget)
        self.btnPesan2 = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan2.setMinimumHeight(20)
        self.btnPesan2.setCursor(QCursor(Qt.PointingHandCursor))
        vbox3.addStretch(3)
        vbox3.addWidget(self.labelPesan2)
        vbox3.addWidget(self.btnPesan2)
        self.group3.setLayout(vbox3)
        self.group3.setMaximumHeight(150)

        self.labelPesan3 = QLabel("Es Teh Panas", self.centralWidget)
        self.btnPesan3 = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan3.setMinimumHeight(20)
        self.btnPesan3.setCursor(QCursor(Qt.PointingHandCursor))
        vbox4.addStretch(3)
        vbox4.addWidget(self.labelPesan3)
        vbox4.addWidget(self.btnPesan3)
        self.group4.setLayout(vbox4)
        self.group4.setMaximumHeight(150)

#grid2
        self.labelPesan4 = QLabel("Nasiaja", self.centralWidget)
        self.btnPesan4 = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan4.setMinimumHeight(20)
        self.btnPesan4.setCursor(QCursor(Qt.PointingHandCursor))
        vbox5.addStretch(3)
        vbox5.addWidget(self.labelPesan4)
        vbox5.addWidget(self.btnPesan4)
        self.group5.setLayout(vbox5)
        self.group5.setMaximumHeight(150)

        self.labelPesan5 = QLabel("Es Teh Panas", self.centralWidget)
        self.btnPesan5 = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan5.setMinimumHeight(20)
        self.btnPesan5.setCursor(QCursor(Qt.PointingHandCursor))
        vbox6.addStretch(3)
        vbox6.addWidget(self.labelPesan5)
        vbox6.addWidget(self.btnPesan5)
        self.group6.setLayout(vbox6)
        self.group6.setMaximumHeight(150)

        self.labelPesan6 = QLabel("Es Teh Panas", self.centralWidget)
        self.btnPesan6 = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan6.setMinimumHeight(20)
        self.btnPesan6.setCursor(QCursor(Qt.PointingHandCursor))
        vbox7.addStretch(3)
        vbox7.addWidget(self.labelPesan6)
        vbox7.addWidget(self.btnPesan6)
        self.group7.setLayout(vbox7)
        self.group7.setMaximumHeight(150)

        self.labelPesan7 = QLabel("Es Teh Panas", self.centralWidget)
        self.btnPesan7 = QPushButton ("Pesan nich", self.centralWidget)
        self.btnPesan7.setMinimumHeight(20)
        self.btnPesan7.setCursor(QCursor(Qt.PointingHandCursor))
        vbox8.addStretch(3)
        vbox8.addWidget(self.labelPesan7)
        vbox8.addWidget(self.btnPesan7)
        self.group8.setLayout(vbox8)
        self.group8.setMaximumHeight(150)


        grid.addWidget(self.group1, 0, 1)
        grid.addWidget(self.group2, 0, 2)
        grid.addWidget(self.group3, 0, 3)
        grid.addWidget(self.group4, 0, 4)
        
        grid.addWidget(self.group5, 1, 1)
        grid.addWidget(self.group6, 1, 2)
        grid.addWidget(self.group7, 1, 3)
        grid.addWidget(self.group8, 1, 4)

#button
        font.setPointSize(10)

        self.btnEdit = QPushButton("Edit Menu", self.centralWidget)
        self.btnEdit.setObjectName("edit")
        self.btnEdit.setFont(font)
        self.btnEdit.move(220,660)

        self.btnTambah = QPushButton("Tambah Menu", self.centralWidget)
        self.btnTambah.setObjectName("tambah")
        self.btnTambah.setFont(font)
        self.btnTambah.move(400,660)



