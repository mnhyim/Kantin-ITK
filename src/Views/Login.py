import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.Class.Autentikasi import Autentikasi
from src.Views.Admin import Admin
from src.Views.Pembeli import Pembeli
from src.Views.Signup import Signup


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()

        layout = QHBoxLayout()
        layout.addItem(self.leftSide())
        layout.addItem(self.rightSide())

    def leftSide(self):
        self.stylesheet = """
        QWidget{
            color: #fff;
            font-family: 'Open Sans';
        }
        QFrame#frameBg{
            background-color: #5f6caf;
        }
        QLabel{
            background-color: rgba(0,0,0,0);
            color: #eee;
        }
        QLineEdit{
            border: 2px solid transparent;
            border-radius: 4;
            color: #333;
        }
        QLineEdit::focus{
            border: 2px solid rgba(255, 133, 102, .95);
        }
        QPushButton#btnLogin{
            background-color: #ffb677;
            border: none;
            border-radius: 4;
            color: #333;
        }
        QPushButton#btnLogin::hover{
            background-color: #ffa377;
        }

        QPushButton#btnLogin:focus{
            background-color: #ff9066;
        }

        QPushButton#btnSignUp{
            background-color: transparent;
            text-decoration: underline;
            border: none;
            border-radius: 4;
            color: #ffb677;
        }
        QPushButton#btnSignUp::hover{
            color: #ffa377;
        }
        QPushButton#btnSignUp::focus{
            color: #ff9066;
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

        self.teksLogin = QLabel("Login", self.frame)
        self.teksLogin.setFont(self.font.textTitle)
        self.teksLogin.setGeometry(150, 100, 100, 50)

        self.ketLogin = QLabel("Silahkan Login dengan menggunakan Email ITK", self.frame)
        self.ketLogin.setGeometry(50, 160, 300, 50)
        self.ketLogin.setScaledContents(True)
        self.ketLogin.setFont(self.font.textSubtitle)
        self.ketLogin.setAlignment(Qt.AlignCenter)
        self.ketLogin.setWordWrap(True)

        self.labelUser = QLabel("Email", self.frame)
        self.labelUser.setGeometry(45, 300, 100, 20)
        self.labelUser.setFont(self.font.textLabel)

        self.labelPassword = QLabel("Password", self.frame)
        self.labelPassword.setGeometry(45, 390, 100, 20)
        self.labelPassword.setFont(self.font.textLabel)

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

        self.btnLogin = QPushButton("Login", self.frame)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setGeometry(45, 490, 100, 20)
        self.btnLogin.resize(320, 45)
        self.btnLogin.setFont(self.font.textLabel)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.clicked.connect(lambda: self.login(self.formEmail.text(), self.formPassword.text()))

        self.btnSignUp = QPushButton("Sign Up", self.frame)
        self.btnSignUp.setObjectName("btnSignUp")
        self.btnSignUp.setGeometry(45, 540, 100, 20)
        self.btnSignUp.resize(320, 45)
        self.font.textLabel.setPointSize(11)
        self.btnSignUp.setFont(self.font.textLabel)
        self.btnSignUp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSignUp.clicked.connect(lambda: self.signUp())

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

        self.header = QLabel("Kantin ITK", self.frame)
        self.header.setObjectName("header")
        self.header.setGeometry(20, 0, 250, 120)
        self.header.setFont(self.font.textTitle)

        self.ket = QLabel(
            "Institut Teknologi Kalimantan, Kokoh berdiri di katulistiwa, Simbol suci kemajuan teknologi, Tak tergantikan di Bumi Borneo, Mantap melangkah menggoreskan karya, Demi meraih cita, Mewujudkan kemandirian bangsa, Kuat dan berdikari",
            self.frame)
        self.ket.setGeometry(20, 100, 900, 200)
        self.ket.setFont(self.font.textSubtitle)
        self.ket.setWordWrap(True)
        self.ket.setAlignment(Qt.AlignJustify)

        self.lb = QLabel(self.frame)
        self.pixmap = QtGui.QPixmap("../Assets/login_illustration.png")
        self.lb.resize(self.width(), self.height())
        self.lb.setPixmap(self.pixmap.scaled(self.lb.size(), QtCore.Qt.KeepAspectRatio))
        self.lb.setGeometry(250, 250, self.width(), self.height())

    def login(self, email, password):
        auth = Autentikasi(email, password)
        auth.login()
        if auth.getStatusLogin() == True:
            if auth.getRoleLogin().value == 1:
                print(auth.getRoleLogin().name)
                self.AdminScreen = Admin()
                self.parent().setCentralWidget(self.AdminScreen)

            elif auth.getRoleLogin().value == 2:
                pass
                # print(auth.getRoleLogin().name)
                # self.PenjualScreen = Penjual()
                # self.parent().setCentralWidget(self.PenjualScreen)

            elif auth.getRoleLogin().value == 3:
                print(auth.getRoleLogin().name)
                self.PembeliScreen = Pembeli()
                self.parent().setCentralWidget(self.PembeliScreen)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Email atau Password Salah")
            msg.setWindowTitle("Error")
            msg.exec_()

    def signUp(self):
        signUpScreen = Signup()
        self.parent().setCentralWidget(signUpScreen)

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
