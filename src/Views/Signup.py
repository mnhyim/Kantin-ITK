import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.Class.EnumClass import JenisAkun
from src.ORM.ormAkun import *


class Signup(QWidget):
    def __init__(self):
        super(Signup, self).__init__()

        layout = QHBoxLayout()
        layout.addItem(self.leftSide())
        layout.addItem(self.rightSide())

    def leftSide(self):
        self.stylesheet = """
        QWidget#leftWidget{
            color: #fff;
            font-family: 'Open Sans';
        }
        QFrame#frameBg{
            background-color: #5f6caf;
        }
        QLabel{
            background-color: rgba(0,0,0,0);
            color:#eee;
        }
        QLineEdit{
            border: 2px solid transparent;
            border-radius: 4;
            color: #333;
        }
        QLineEdit::focus{
            border: 2px solid rgba(255, 133, 102, .95);
        }
        QPushButton#btnSignUp{
            background-color: #ffb677;
            border: none;
            border-radius: 4;
            color: #333;
        }
        QPushButton#btnSignUp::hover{
            background-color: #ffa377;
        }

        QPushButton#btnSignUp:focus{
            background-color: #ff9066;
        }
        QComboBox#jenisAkun{
            color: #333;
            border: none;
            border-radius: 4;
        }
        
    
        """
        self.font = self.fontTemplate()

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("leftWidget")
        self.centralWidget.setFixedSize(420, 720)
        self.centralWidget.setStyleSheet(self.stylesheet)

        self.frame = QFrame(self.centralWidget)
        self.frame.setFixedSize(420, 900)
        self.frame.setObjectName("frameBg")
        self.frame.setLayoutDirection(Qt.LeftToRight)

        self.teksLogin = QLabel("Sign Up", self.frame)
        self.teksLogin.setFont(self.font.textTitle)
        self.teksLogin.setGeometry(150, 80, 130, 50)

        self.ketLogin = QLabel("Silahkan daftar terlebih dahulu", self.frame)
        self.ketLogin.setGeometry(50, 140, 300, 50)
        self.ketLogin.setScaledContents(True)
        self.ketLogin.setFont(self.font.textSubtitle)
        self.ketLogin.setAlignment(Qt.AlignCenter)
        self.ketLogin.setWordWrap(True)

        self.labelNama = QLabel("Nama", self.frame)
        self.labelNama.setGeometry(45, 210, 100, 20)
        self.labelNama.setFont(self.font.textLabel)

        self.labelUser = QLabel("Email", self.frame)
        self.labelUser.setGeometry(45, 300, 100, 20)
        self.labelUser.setFont(self.font.textLabel)

        self.labelPassword = QLabel("Password", self.frame)
        self.labelPassword.setGeometry(45, 390, 100, 20)
        self.labelPassword.setFont(self.font.textLabel)

        self.labelJenisAkun = QLabel("Jenis Akun", self.frame)
        self.labelJenisAkun.setGeometry(45, 480, 100, 20)
        self.labelJenisAkun.setFont(self.font.textLabel)

        self.formNama = QLineEdit(self.frame)
        self.formNama.setGeometry(45, 240, 100, 20)
        self.formNama.setStyleSheet("background-color: #fff")
        self.formNama.resize(320, 40)
        self.formNama.setPlaceholderText("Masukkan Nama Anda")
        self.formNama.setFont(self.font.textSubtitle)
        self.formNama.setTextMargins(12, 5, 12, 5)

        self.formEmail = QLineEdit(self.frame)
        self.formEmail.setGeometry(45, 330, 100, 20)
        self.formEmail.setStyleSheet("background-color: #fff")
        self.formEmail.resize(320, 40)
        self.formEmail.setPlaceholderText("Masukkan Email")
        self.formEmail.setFont(self.font.textSubtitle)
        self.formEmail.setTextMargins(12, 5, 12, 5)

        self.formPassword = QLineEdit(self.frame)
        self.formPassword.setGeometry(45, 420, 100, 20)
        self.formPassword.setStyleSheet("background-color: #fff")
        self.formPassword.resize(320, 40)
        self.formPassword.setPlaceholderText("Masukkan Password")
        self.formPassword.setFont(self.font.textSubtitle)
        self.formPassword.setTextMargins(12, 5, 12, 5)
        self.formPassword.setEchoMode(QLineEdit.Password)

        self.formJenisAkun = QComboBox(self.frame)
        self.formJenisAkun.setGeometry(45, 510, 100, 20)
        self.formJenisAkun.setObjectName("jenisAkun")
        self.formJenisAkun.resize(320, 40)
        for i in JenisAkun:
            self.formJenisAkun.addItem(i.name)
        self.formJenisAkun.setFont(self.font.textSubtitle)

        self.btnSignUp = QPushButton("Sign Up", self.frame)
        self.btnSignUp.setObjectName("btnSignUp")
        self.btnSignUp.setGeometry(45, 600, 100, 20)
        self.btnSignUp.resize(320, 45)
        self.font.textLabel.setPointSize(11)
        self.btnSignUp.setFont(self.font.textLabel)
        self.btnSignUp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSignUp.clicked.connect(lambda: self.signupUser())

    def rightSide(self):
        self.stylesheet = """
               QWidget{
                   color: #333;
                   font-family: 'Open Sans';
                   background-color: rgba(0,0,0,0)
               }
               QLabel{
                   font-family: 'Raleway';
               }
               """
        self.font = self.fontTemplate()

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("rightWidget")
        self.centralWidget.move(420, 0)
        self.centralWidget.setStyleSheet(self.stylesheet)
        self.centralWidget.setFixedSize(950, 720)

        self.frame = QFrame(self.centralWidget)
        self.frame.setFixedSize(950, 720)
        self.frame.setObjectName("frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)

        self.lb = QLabel(self.frame)
        self.pixmap = QtGui.QPixmap("../Assets/login_illustration.png")
        self.lb.resize(self.width(), self.height())
        self.lb.setPixmap(self.pixmap.scaled(self.lb.size(), QtCore.Qt.KeepAspectRatio))
        self.lb.setGeometry(250, 250, self.width(), self.height())

    def signupUser(self):
        nama = self.formNama.text()
        email = self.formEmail.text()
        password = self.formPassword.text()
        jenisAkun = self.formJenisAkun.currentText()

        if jenisAkun == "Admin" and (nama != "" and email != "" and password != ""):
            print("masuk ke 1")
            try:
                AdminOrm(nama, email, password, jenisAkun).insert()
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("User {} berhasil dibuat dengan role {}".format(nama, jenisAkun))
                msg.exec_()

                from src.Views.Login import Login
                loginScreen = Login()
                self.parent().setCentralWidget(loginScreen)
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(e)
                msg.setWindowTitle("Error")
                msg.exec_()

        elif jenisAkun == "Penjual" and (nama != "" and email != "" and password != ""):
            print("masuk ke 2")
            try:
                PenjualOrm(nama, email, password, jenisAkun, 0).insert()
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("User {} berhasil dibuat dengan role {}".format(nama, jenisAkun))
                msg.exec_()

                from src.Views.Login import Login
                loginScreen = Login()
                self.parent().setCentralWidget(loginScreen)
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(e)
                msg.setWindowTitle("Error")
                msg.exec_()
        elif jenisAkun == "Pembeli" and (nama != "" and email != "" and password != ""):
            print("masuk ke 3")
            try:
                PembeliOrm(nama, email, password, jenisAkun, 0).insert()
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("User {} berhasil dibuat dengan role {}".format(nama, jenisAkun))
                msg.exec_()

                from src.Views.Login import Login
                loginScreen = Login()
                self.parent().setCentralWidget(loginScreen)
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(e)
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("isi kolomnya bro")
            msg.setWindowTitle("Error")
            msg.exec_()

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
