import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class LihatPenjual(QWidget):
    def __init__(self):
        super(LihatPenjual, self).__init__()

        # self.sidebarUI()
        self.rightSide()
        # self.createHorizontalLayout()

    def rightSide(self):
        self.stylesheet = """
        QWidget{
            font-family: 'Open Sans';
            color: #030303;
        }
        QLabel#title{
            background-color: #0314ff;
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
        QPushButton#tambahakun{
            background-color: #0314ff;
            border: none;
            border-radius: 4;
            color: #0a0807;
        }
        QPushButton#tambahakun::hover{
            background-color: #0c1b7d;
        }
        QPushButton#editprofil{
            background-color: #e3d408;
            border: none;
            border-radius: 4;
            color: #0a0807;
        }
        QPushButton#editprofil::hover{
            background-color: #cfc205;
        }
        QPushButton#hapusakun{
            background-color: #ff1a0a;
            border: none;
            border-radius: 4;
            color: #0a0807;
        }
        QPushButton#hapusakun::hover{
            background-color: #db1304;
        }
        
        """

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("mainbar")
        # self.centralWidget.move(400, 0)
        self.centralWidget.setStyleSheet(self.stylesheet)
        self.centralWidget.setFixedSize(720, 720)

        font = QFont("Arial")
        font.setPointSize(20)
        
        self.labelTitle = QLabel("Penjual", self.centralWidget)
        self.labelTitle.setObjectName("title")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setFont(font)

        self.group = QGroupBox()
        vertikal = QVBoxLayout()    
        self.radiobtn = QButtonGroup()
        self.list = ["Andi","gaple","habib","Hacim","Andi","gaple","habib","Hacim","Andi","gaple","habib","Hacim","Andi","gaple","habib","Hacim","Andi","gaple","habib","Hacim"]
        for i in (self.list):
            font.setPointSize(15)
            self.labelNama = QRadioButton(i)
            self.labelNama.setStyleSheet('QRadioButton{font: 15pt Helvetica MS;} QRadioButton::indicator { width: 30px; height: 30px;};')
            self.radiobtn.addButton(self.labelNama)
            vertikal.addWidget(self.labelNama)

        self.group.setLayout(vertikal)
        scroll = QScrollArea()
        scroll.setWidget(self.group)
        scroll.setWidgetResizable(True)
        #scroll.setHorizontalScrollBarPolicy(Qt::scr)

        self.btnBack = QPushButton("Kembali", self.centralWidget)
        self.btnBack.setObjectName("back")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnAddacc = QPushButton("Tambah Akun", self.centralWidget)
        self.btnAddacc.setObjectName("tambahakun")
        self.btnAddacc.setFixedSize(200, 40)
        self.btnAddacc.setFont(font)
        self.btnAddacc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddacc.clicked.connect(self.btn)

        self.btnEditprofil = QPushButton("Edit Profil", self.centralWidget)
        self.btnEditprofil.setObjectName("editprofil")
        self.btnEditprofil.setFixedSize(200, 40)
        self.btnEditprofil.setFont(font)
        self.btnEditprofil.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEditprofil.clicked.connect(self.btn)

        self.btnDelacc = QPushButton("Hapus Akun", self.centralWidget)
        self.btnDelacc.setObjectName("hapusakun")
        self.btnDelacc.setFixedSize(200, 40)
        self.btnDelacc.setFont(font)
        self.btnDelacc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDelacc.clicked.connect(self.btn)

        layoutHor1 = QHBoxLayout()
        layoutHor1.addWidget(self.labelTitle)
        

        layoutHor2 = QHBoxLayout()
        layoutHor2.addWidget(self.btnAddacc)
        layoutHor2.addWidget(self.btnEditprofil)
        layoutHor2.addWidget(self.btnDelacc)

        layoutBack = QHBoxLayout()
        layoutBack.addWidget(self.btnBack, alignment=Qt.AlignLeft)

        vertical = QVBoxLayout(self.centralWidget)
        vertical.addLayout(layoutBack)
        vertical.addStretch()
        vertical.addLayout(layoutHor1)
        vertical.addWidget(scroll)
        for i in range(20):
            vertical.addStretch()
        vertical.addLayout(layoutHor2)

        self.centralWidget.setLayout(vertical)

    #test penggunaan button
    def btn(self):
        self.checked = self.radiobtn.checkedButton().text()
        self.msg = QMessageBox(self.centralWidget)
        self.msg.setText(f"pilihan anda adalah {self.checked}")
        self.msg.exec_()
