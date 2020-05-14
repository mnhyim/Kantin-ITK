import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class EditAkun(QWidget):
    def __init__(self):
        super(EditAkun, self).__init__()

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
        QPushButton#simpan{
            background-color: #c2c0bf;
            border: none;
            border-radius: 4;
            color: #0a0807;
        }
        QPushButton#simpan::hover{
            background-color: #ada9a7;
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
 
        self.labelName = QLabel("Nama               :",self.centralWidget)
        self.labelName.setFont(font)
        self.leditName = QLineEdit(self.centralWidget)
        self.leditName.setText("")
        self.leditName.setFont(font)
        
        self.labelEmail = QLabel("Email                :",self.centralWidget)
        self.labelEmail.setFont(font)
        self.leditEmail = QLineEdit(self.centralWidget)
        self.leditEmail.setText("")
        self.leditEmail.setFont(font)

        self.labelUsername = QLabel("Username       :",self.centralWidget)
        self.labelUsername.setFont(font)
        self.leditUsername = QLineEdit(self.centralWidget)
        self.leditUsername.setText("")
        self.leditUsername.setFont(font)

        self.labelPassword = QLabel("Password        :",self.centralWidget)
        self.labelPassword.setFont(font)  
        self.leditPassword = QLineEdit(self.centralWidget)
        self.leditPassword.setText("")
        self.leditPassword.setFont(font)  

        self.btnBack = QPushButton("Kembali", self.centralWidget)
        self.btnBack.setObjectName("back")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnSave = QPushButton("Simpan", self.centralWidget)
        self.btnSave.setObjectName("simpan")
        self.btnSave.setFixedSize(200, 40)
        self.btnSave.setFont(font)
        self.btnSave.setCursor(QCursor(Qt.PointingHandCursor))

        layoutHor1 = QHBoxLayout()
        layoutHor1.addWidget(self.labelName)
        layoutHor1.addWidget(self.leditName)
        layoutHor1.setSpacing(51)

        layoutHor2 = QHBoxLayout()
        layoutHor2.addWidget(self.labelEmail)
        layoutHor2.addWidget(self.leditEmail)
        layoutHor2.setSpacing(50)

        layoutHor3 = QHBoxLayout()
        layoutHor3.addWidget(self.labelUsername)
        layoutHor3.addWidget(self.leditUsername)
        layoutHor3.setSpacing(52)

        layoutHor4 = QHBoxLayout()
        layoutHor4.addWidget(self.labelPassword)
        layoutHor4.addWidget(self.leditPassword)
        layoutHor4.setSpacing(51)

        layoutHor = QHBoxLayout()
        layoutHor.addWidget(self.btnSave, alignment=Qt.AlignCenter)

        layoutBack = QHBoxLayout()
        layoutBack.addWidget(self.btnBack, alignment=Qt.AlignLeft)

        vertical = QVBoxLayout(self.centralWidget)
        vertical.addLayout(layoutBack)
        vertical.addStretch()
        vertical.addLayout(layoutHor1)
        vertical.addLayout(layoutHor2)
        vertical.addLayout(layoutHor3)
        vertical.addLayout(layoutHor4)
        for i in range(20):
            vertical.addStretch()
        vertical.addLayout(layoutHor)

        self.centralWidget.setLayout(vertical)
