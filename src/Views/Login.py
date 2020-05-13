import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Sidebar import Sidebar


class Login(QMainWindow):
    def __init__(self, *args, **kargs):
        super(Login, self).__init__(*args, **kargs)

        layout = QHBoxLayout()
        layout.addItem(self.leftSide())
        layout.addItem(self.rightSide())

    def leftSide(self):
        self.stylesheet = """
        QWidget{
            color: #fff;
            font-family: 'Open Sans';
        }
        QFrame{
            background-color: #5f6caf;
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
    
        """
        self.font = self.fontTemplate()

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("leftWidget")
        self.centralWidget.setFixedSize(420, 720)
        self.centralWidget.setStyleSheet(self.stylesheet)

        self.frame = QFrame(self.centralWidget)
        self.frame.setFixedSize(420, 900)
        self.frame.setObjectName("frame")
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

        self.email = QLineEdit(self.frame)
        self.email.setGeometry(45, 330, 100, 20)
        self.email.setStyleSheet("background-color: #fff")
        self.email.resize(320, 40)
        self.email.setPlaceholderText("Masukkan Email")
        self.email.setFont(self.font.textSubtitle)
        self.email.setTextMargins(12, 5, 12, 5)

        self.password = QLineEdit(self.frame)
        self.password.setGeometry(45, 420, 100, 20)
        self.password.setStyleSheet("background-color: #fff")
        self.password.resize(320, 40)
        self.password.setPlaceholderText("Masukkan Password")
        self.password.setFont(self.font.textSubtitle)
        self.password.setTextMargins(12, 5, 12, 5)
        self.password.setEchoMode(QLineEdit.Password)

        self.btnLogin = QPushButton("Login", self.frame)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setGeometry(45, 490, 100, 20)
        self.btnLogin.resize(320, 45)
        self.btnLogin.setFont(self.font.textLabel)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.clicked.connect(self.mainPage)

    def rightSide(self):
        self.stylesheet = """
        QWidget{
            color: #333;
            font-family: 'Open Sans';
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
            "Institut Teknologi Kalimantan, Kokoh berdiri di katulistiwa, Simbol suci kemajuan teknologi, Tak tergantikan di Bumi Borneo, Mantap melangkah menggoreskan karya, Demi meraih cita, Mewujudkan kemandirian bangsa, Kuat dan berdikari",self.frame)
        self.ket.setGeometry(20, 100, 900, 200)
        self.ket.setFont(self.font.textSubtitle)
        self.ket.setWordWrap(True)
        self.ket.setAlignment(Qt.AlignJustify)

    def mainPage(self):
        self.side = Sidebar()
        self.parent().setCentralWidget(self.side)
        # self.hide()

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
