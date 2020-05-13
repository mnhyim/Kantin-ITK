import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QGridLayout, QLineEdit, QPushButton


class LoginView(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Login")

        # Grid layout yang akan diisi dengan 2 Vertical Layout
        self.ParentLayout = QHBoxLayout()
        # Set jarak antar widget di qLayout
        self.ParentLayout.setSpacing(0)
        # Menghilangkan margin antara gLayout dengan Window
        self.ParentLayout.setContentsMargins(0, 0, 0, 0)
        # Menambahkan widget frameKiri yang direturn dari fungsi leftSide
        self.ParentLayout.addWidget(self.leftSide())
        # Menambahkan widget frameKanan yang direturn dari fungsi rightSide
        self.ParentLayout.addWidget(self.rightSide())
        # Set layout object LoginView ke gLayout
        self.setLayout(self.ParentLayout)

    def leftSide(self):
        # Membuat object Vertical layout dan set Alignment ke tengah
        self.vLayoutKiri = QVBoxLayout()
        self.vLayoutKiri.setAlignment(Qt.AlignCenter)
        # Add widget ke layout
        self.leftWidget = self.widgetLogin()
        self.vLayoutKiri.addWidget(self.leftWidget.loginTitle)
        self.vLayoutKiri.addWidget(self.leftWidget.ketLogin)
        self.vLayoutKiri.addWidget(self.leftWidget.labelEmail)
        self.vLayoutKiri.addWidget(self.leftWidget.formEmail)
        self.vLayoutKiri.addWidget(self.leftWidget.labelPassword)
        self.vLayoutKiri.addWidget(self.leftWidget.formPassword)
        self.vLayoutKiri.addWidget(self.leftWidget.btnLogin)

        # Bikin frame, set stylenya dan mengassign layout sebelumnya ke frame tsb
        self.frameKiri = QFrame()
        self.frameKiri.setFixedWidth(350)
        self.frameKiri.stylesheet = """
                QWidget{
                    color: #fff;
                    font-family: 'Open Sans';
                }
                QFrame{
                    background-color: #5f6caf;
                }
                QLineEdit{
                    border: none;
                    border-radius: 4px;
                    color: #333;
                }
                QPushButton#btnLogin{
                    background-color: #ffb677;
                    border: none;
                    border-radius: 4px;
                    color: #333;
                }
                QPushButton#btnLogin::hover{
                    background-color: #ffa377;
                }
                """
        self.frameKiri.setStyleSheet(self.frameKiri.stylesheet)
        self.frameKiri.setLayout(self.vLayoutKiri)

        # Return object frameKiri
        return self.frameKiri

    def rightSide(self):
        # Membuat object Vertical layout dan set Alignment ke tengah
        self.vLayoutKanan = QVBoxLayout()
        self.vLayoutKanan.setAlignment(Qt.AlignTop)
        # Add widget ke layout
        self.vLayoutKanan.addWidget(QLabel("Login"))
        self.vLayoutKanan.addWidget(QLabel("Silahkan Login dengan menggunakan Email ITK"))

        # Bikin frame, set stylenya dan mengassign layout sebelumnya ke frame tsb
        self.frameKanan = QFrame()
        self.frameKanan.stylesheet = """
                QWidget{
                    color: #333;
                    background-color:  #000;
                    font-family: 'Open Sans';
                }
                QLabel#header{
                    font-family: 'Raleway';
                }
                """
        self.frameKanan.setStyleSheet(self.frameKanan.stylesheet)
        self.frameKanan.setLayout(self.vLayoutKanan)

        return self.frameKanan

    def widgetLogin(self):
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

        self.loginTitle = QLabel("Login")
        self.loginTitle.setFont(self.textTitle)

        self.ketLogin = QLabel("Silahkan Login dengan menggunakan Email ITK")
        self.ketLogin.setFont(self.textSubtitle)
        self.ketLogin.setWordWrap(True)

        self.labelEmail = QLabel("Email")
        self.labelEmail.setFont(self.textLabel)

        self.labelPassword = QLabel("Password")
        self.labelPassword.setFont(self.textLabel)

        self.formEmail = QLineEdit()
        self.formEmail.setPlaceholderText("Masukkan Email")
        self.formEmail.setFont(self.textPlaceholder)
        self.formEmail.setTextMargins(12, 5, 12, 5)

        self.formPassword = QLineEdit()
        self.formPassword.setPlaceholderText("Masukkan Password")
        self.formPassword.setFont(self.textPlaceholder)
        self.formPassword.setTextMargins(12, 5, 12, 5)
        self.formPassword.setEchoMode(QLineEdit.Password)

        self.btnLogin = QPushButton("Login")
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setFont(self.textLabel)
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))

        return self
