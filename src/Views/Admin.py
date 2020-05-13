import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Admin(QMainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        
       # self.sidebarUI()
        self.rightSide()
        #self.createHorizontalLayout()
        

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
        QPushButton#tambahakun{
            background-color: #0314ff;
            border: none;
            color: #0a0807;
        }
        QPushButton#tambahakun::hover{
            background-color: #0c1b7d;
        }
        QPushButton#editprofil{
            background-color: #fff34c;
            border: none;
            color: #0a0807;
        }
        QPushButton#editprofil::hover{
            background-color: #a1972e;
        }
        QPushButton#hapusakun{
            background-color: #ff2f05;
            border: none;
            color: #0a0807;
        }
        QPushButton#hapusakun::hover{
            background-color: #a81c00;
        }

        
        """

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("mainbar")
        self.centralWidget.move(400, 0)
        self.centralWidget.setStyleSheet(self.stylesheet)
        self.centralWidget.setFixedSize(720, 720)


        font = QFont("Arial") 
        font.setPointSize(20)
        font.setWordSpacing(0)
        
        
        self.labelId = QLabel("ID", self.centralWidget)
        self.labelId.setFont(font)

        self.labelx = QLabel(":", self.centralWidget)
        self.labelx.setFont(font)

        self.labelIdfield = QLabel("01", self.centralWidget)
        self.labelIdfield.setFont(font)
        
        self.labelNama = QLabel("Nama", self.centralWidget)
        self.labelNama.setFont(font)

        self.labely = QLabel(":", self.centralWidget)
        self.labely.setFont(font)

        self.labelNamafield = QLabel("Admin", self.centralWidget)
        self.labelNamafield.setFont(font)

        self.btnBack = QPushButton("Kembali", self.centralWidget)
        self.btnBack.setObjectName("back")
        self.btnBack.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnAddacc = QPushButton("Tambah Akun",self.centralWidget)
        self.btnAddacc.setObjectName("tambahakun")
        self.btnAddacc.setFixedHeight(40)
        self.btnAddacc.setFont(font)
        self.btnAddacc.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnEditprof = QPushButton("Edit Profil",self.centralWidget)
        self.btnEditprof.setObjectName("editprofil")
        self.btnEditprof.setFixedHeight(40)
        self.btnEditprof.setFont(font)
        self.btnEditprof.setCursor(QCursor(Qt.PointingHandCursor))

        self.btnDelacc = QPushButton("Hapus Akun",self.centralWidget)
        self.btnDelacc.setObjectName("hapusakun")
        self.btnDelacc.setFixedHeight(40)
        self.btnDelacc.setFont(font)
        self.btnDelacc.setCursor(QCursor(Qt.PointingHandCursor))
        
        layoutHor1 = QHBoxLayout()
        layoutHor1.addWidget(self.labelId)
        layoutHor1.addWidget(self.labelx)
        layoutHor1.addWidget(self.labelIdfield)
        layoutHor1.addStretch()
         
        
        layoutHor2 = QHBoxLayout()
        layoutHor2.addWidget(self.labelNama)
        layoutHor2.addWidget(self.labely)
        layoutHor2.addWidget(self.labelNamafield)
        layoutHor2.addStretch()

        layout = QHBoxLayout()
        layout.addWidget(self.btnDelacc)
        layout.addWidget(self.btnAddacc)
        layout.addWidget(self.btnEditprof)

        layoutBack = QHBoxLayout()
        layoutBack.addWidget(self.btnBack, alignment = Qt.AlignLeft)

        vertical = QVBoxLayout(self.centralWidget)
        vertical.addLayout(layoutBack)
        vertical.addStretch() 
        vertical.addLayout(layoutHor1)
        vertical.addLayout(layoutHor2)
        for i in range(20):
            vertical.addStretch()
        vertical.addLayout(layout)

        self.centralWidget.setLayout(vertical)

