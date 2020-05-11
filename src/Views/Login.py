import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Login:
    def __init__(self):
        super().__init__()
        self.app = QApplication([])
        self.mainWindow = QMainWindow()
        self.mainWindow.setWindowTitle("Login")
        self.mainWindow.setGeometry(140,50,1100,650)
        self.mainWindow.setStyleSheet("background-color: #edf7fa")

        self.leftSide()
        self.rightSide()

        self.mainWindow.show()
        sys.exit(self.app.exec_())

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
            border: none;
            border-radius: 4;
            color: #333;
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
        """
        self.centralWidget = QWidget(self.mainWindow)
        self.centralWidget.setObjectName("leftWidget")
        self.centralWidget.setFixedSize(420,650)
        self.centralWidget.setStyleSheet(self.stylesheet)

        self.verticalLay = QVBoxLayout(self.centralWidget)
        self.verticalLay.setObjectName("verticalLayout")

        self.frame = QFrame(self.centralWidget)
        self.frame.setFixedSize(420, 650)
        self.frame.setObjectName("frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)

        self.vertical = QVBoxLayout(self.frame)
        self.vertical.setObjectName("vLayout")

        font = QFont()
        font.setPointSize(28)
        font.setWeight(75)

        self.teksLogin = QLabel("Login", self.frame)
        self.teksLogin.setFont(font)
        self.teksLogin.setGeometry(150, 100, 100, 50)

        font.setPointSize(12)
        font.setWeight(60)
        self.ketLogin = QLabel("Silahkan Login dengan menggunakan Email ITK", self.frame)
        self.ketLogin.setGeometry(50, 160, 300, 50)
        self.ketLogin.setScaledContents(True)
        self.ketLogin.setFont(font)
        self.ketLogin.setAlignment(Qt.AlignCenter)
        self.ketLogin.setWordWrap(True)

        font.setPointSize(14)
        font.setWeight(75)
        self.labelUser = QLabel("Email", self.frame)
        self.labelUser.setGeometry(45, 300, 100, 20)
        self.labelUser.setFont(font)

        self.labelPassword = QLabel("Password", self.frame)
        self.labelPassword.setGeometry(45, 390, 100, 20)
        self.labelPassword.setFont(font)

        font.setPointSize(12)
        font.setWeight(20)
        self.email = QLineEdit(self.frame)
        self.email.setGeometry(45, 330, 100, 20)
        self.email.setStyleSheet("background-color: #fff")
        self.email.resize(320, 38)
        self.email.setPlaceholderText("Masukkan Email")
        self.email.setFont(font)
        self.email.setTextMargins(12, 5 , 12, 5)

        self.password = QLineEdit(self.frame)
        self.password.setGeometry(45, 420, 100, 20)
        self.password.setStyleSheet("background-color: #fff")
        self.password.resize(320,40)
        self.password.setPlaceholderText("Masukkan Password")
        self.password.setFont(font)
        self.password.setTextMargins(12, 5, 12, 5)
        self.password.setEchoMode(QLineEdit.Password)

        font.setPointSize(12)
        font.setWeight(75)
        self.btnLogin = QPushButton("Login",self.frame)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setGeometry(45, 490, 100, 20)
        self.btnLogin.resize(320,45)
        self.btnLogin.setFont(font)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))

    def rightSide(self):
        self.stylesheet = """
        QWidget{
            color: #333;
            font-family: 'Open Sans';
        }
        QLabel#header{
            font-family: 'Raleway';
        }
        """
        self.centralWidget = QWidget(self.mainWindow)
        self.centralWidget.setObjectName("rightWidget")
        self.centralWidget.move(420, 0)
        self.centralWidget.setStyleSheet(self.stylesheet)
        # self.centralWidget.setStyleSheet("background-color:red")
        self.centralWidget.setFixedSize(680, 650)

        self.frame = QFrame(self.centralWidget)
        self.frame.setFixedSize(680, 650)
        self.frame.setObjectName("frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)

        font = QFont()
        font.setPointSize(28)
        font.setWeight(75)

        self.header = QLabel("Kantin ITK", self.frame)
        self.header.setObjectName("header")
        self.header.setGeometry(20, 0, 250, 120)
        self.header.setFont(font)

        font.setPointSize(12)
        font.setWeight(40)
        self.ket = QLabel("Lorem ipsum dolor sit amet consectetur adipisicing elit. Labore dolorum animi aliquam magnam, distinctio quas harum nostrum ea id sit sint laudantium officia quis quibusdam nobis expedita neque voluptatem culpa alias? Iure, quo iusto quia quis voluptatum consectetur adipisci numquam consequuntur. Quisquam, alias labore totam hic quae veniam distinctio, earum soluta nulla aliquid deserunt incidunt.", self.frame)
        self.ket.setGeometry(20, 100, 630, 200)
        self.ket.setFont(font)
        self.ket.setWordWrap(True)
        self.ket.setAlignment(Qt.AlignJustify)

        # self.gambar = QLabel(self.frame)
        # self.gambar.setPixmap(QPixmap("assets/img/h.jpg"))
        # self.gambar.move(0, 250)
        # self.gambar.setFixedSize(700, 400)
        
Login()
