from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.Views._old.Penjual_Tambah_Menu import TambahMenu
from src.Views._old.Penjual_Edit_Menu import EditMenu
from src.Views._old.Penjual_Hapus_Menu import HapusMenu


class PenjualUi(QMainWindow):
    def __init__(self):
        super(PenjualUi, self).__init__()

        self.font = self.fontTemplate()

        self.tab1 = TambahMenu()
        self.tab2 = EditMenu()
        self.tab3 = HapusMenu()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.leftSide())
        main_layout.addWidget(self.rightSide())
        main_layout.setStretch(0, 70)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def leftSide(self):
        self.stylesheet = """
        QWidget#left{
            font-family: 'Open Sans';
            color: #fff;
            background-color: #5f6caf;
        }
        QPushButton{
            border: none;
            background-color: #5f6caf;
            font-size: 16px;
            font-weight: 500;
            padding: 24px;
            color: #fff;
        }
        QPushButton::hover, QPushButton::focus{
            color: #ffb677;
        }
        QPushButton::focus{
            background-color: #54609b;
        }
        QPushButton#logout{
            background-color: #ffb677;
            border: none;
            border-radius: 4;
            color: #333;
        }
        QPushButton#logout::hover{
            background-color: #ffa377;
        }

        QPushButton#logout:focus{
            background-color: #ff9066;
        }
        QLabel{
            background-color: transparent;
            color: #fff;
        }
        QLabel#title{
            font-family: 'Raleway';
            font-size: 32px;
            font-weight: bold;
        }
        QLabel#subtitle{
            font-size: 20px;
            fontweight: medium;
        }
        QComboBox{
            background-color: #fff;
            color: #333;
            border: none;
            border-radius: 4;
        }
        """

        # Buttons
        self.btnTambah = QPushButton('Tambah Menu', self)
        self.btnMakanan.setFont(self.font.textLabel)
        self.btnMakanan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMakanan.clicked.connect(lambda: self.right_widget.setCurrentIndex(0))

        self.btnEdit = QPushButton('Edit Menu', self)
        self.btnMinuman.setFont(self.font.textLabel)
        self.btnMinuman.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMinuman.clicked.connect(lambda: self.right_widget.setCurrentIndex(1))

        self.btnHapus = QPushButton('Hapus Menu', self)
        self.btnTransaksi.setFont(self.font.textLabel)
        self.btnTransaksi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnTransaksi.clicked.connect(lambda: self.right_widget.setCurrentIndex(2))


        self.btnLogout = QPushButton('Logout', self)
        self.btnLogout.setObjectName("logout")
        self.btnLogout.setFont(self.font.textLabel)
        self.btnLogout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogout.clicked.connect(self.buttonLogout)
        # Widgets
        self.textNama = QLabel("Andisul")
        self.textNama.setFont(self.font.textTitle)
        self.textUang = QLabel("Rp. 2.000.000")
        self.textUang.setFont(self.font.textSubtitle)

        self.frame = QFrame()
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setObjectName("frame")

        left_layout = QVBoxLayout(self.frame)
        left_layout.addWidget(self.textNama)
        left_layout.addWidget(self.textUang)
        left_layout.addStretch(1)
        left_layout.addWidget(self.btnTambah)
        left_layout.addWidget(self.btnEdit)
        left_layout.addWidget(self.btnHapus)
        left_layout.addStretch(1)
        left_layout.addWidget(self.btnLogout)
        left_layout.addStretch(0)

        left_widget = QWidget()
        left_widget.setObjectName("left")
        left_widget.setStyleSheet(self.stylesheet)
        left_widget.setLayout(left_layout)
        return left_widget

    def rightSide(self):
        self.style = """
        QTabBar::tab{
            width: 0;
            height: 0;
            margin: 0;
            padding: 0;
            border: none;
        }
        """
        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet(self.style)

        return self.right_widget

    def buttonLogout(self):
        from src.Views._old.Login import Login

        self.back = Login()
        self.parent().setCentralWidget(self.back)

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