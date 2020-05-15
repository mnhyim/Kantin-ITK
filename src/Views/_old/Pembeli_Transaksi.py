from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# from src.Class.Pembeli import Pembeli
# from src.ORM.ormTransaksi import TransaksiOrm
from src.Class.Transaksi import *

class PembeliTransaksi(QWidget):
    def __init__(self):
        super(PembeliTransaksi, self).__init__()

        self.rightSide()

        # windowLay = QVBoxLayout()
        # windowLay.addWidget(self.hGroup)
        # self.setLayout(windowLay)


    def rightSide(self):
        self.stylesheet = """
            QWidget{
                font-family: 'Open Sans';
                color: #030303;
            }
            QLabel#title{
                font-weight: bold;
                font-size: 14px;
                
            }
            QPushButton{
                font-size: 16px;
                font-weight: 500;
                border-radius : 4;
            }
            QPushButton#batal{
                background-color: #e0dad2;
                border: none;
                color: #0a0807;
            }
            QPushButton#bayar{
                background-color: blue;
                border: none
            }

        """
        self.widget = QWidget(self)
        self.widget.setStyleSheet(self.stylesheet)
        self.widget.setFixedSize(980, 720)

        # self.hGroup = QGroupBox()
        # layout = QGridLayout()
        # layout.setVerticalSpacing(2)
        # layout.setHorizontalSpacing(5)
        # layout.setColumnStretch(0, 2)
        # layout.setColumnStretch(1, 2)
        # layout.setColumnStretch(2,2)
        # layout.setColumnStretch(3, 2)
        # layout.setColumnStretch(4, 2)
        # layout.setRowStretch(0, 0)
        # layout.setRowStretch(1, 0)
        # layout.setRowStretch(2, 1)
        # layout.setRowStretch(3, 1)
        # layout.setRowStretch(4, 1)

        hlay1 = QHBoxLayout()
        self.labelPesanan = QLabel("Pesanan", self.widget)
        self.labelPesanan.setObjectName("title")
        self.labelHarga = QLabel("Harga",self.widget)
        self.labelHarga.setObjectName("title")
        self.labelBanyak = QLabel("Banyak",self.widget)
        self.labelBanyak.setObjectName("title")
        hlay1.addWidget(self.labelPesanan)
        hlay1.addWidget(self.labelHarga)
        hlay1.addWidget(self.labelBanyak)

        hlay2 = QHBoxLayout()
        self.textPesanan = QLabel("Tes",self.widget)
        self.textHarga = QLabel("Rp. 100",self.widget)
        self.spinBanyak = QSpinBox()
        hlay2.addWidget(self.textPesanan)
        hlay2.addWidget(self.textHarga)
        hlay2.addWidget(self.spinBanyak)

        hlay3 = QHBoxLayout()
        self.labelTotal = QLabel("Total",self.widget)
        self.labelTotal.setObjectName("title")
        self.textTotal = QLabel("Rp. 100",self.widget)
        hlay3.addWidget(self.labelTotal)
        hlay3.addWidget(self.textTotal)

        hlay4 = QHBoxLayout()
        self.labelJenis = QLabel("Jenis Pembayaran",self.widget)
        self.labelJenis.setObjectName("title")
        self.cmbJenis = QComboBox(self.widget)
        self.cmbJenis.addItem("Cash")
        self.cmbJenis.addItem("Saldo")
        hlay4.addWidget(self.labelJenis)
        hlay4.addWidget(self.cmbJenis)

        hlay5 = QHBoxLayout()
        self.btnBatal = QPushButton("Batal",self.widget)
        self.btnBayar = QPushButton("Bayar",self.widget)
        self.btnBatal.setObjectName("batal")
        self.btnBayar.setObjectName("bayar")
        self.btnBayar.clicked.connect(self.submit)
        # hlay5.addStretch(0)
        hlay5.addWidget(self.btnBatal, alignment=Qt.AlignRight)
        hlay5.addWidget(self.btnBayar, alignment=Qt.AlignRight)


        vLay = QVBoxLayout(self.widget)
        vLay.addLayout(hlay1)
        vLay.addStretch(0)
        vLay.addLayout(hlay2)
        vLay.addStretch(0)
        vLay.addLayout(hlay3)
        vLay.addStretch(0)
        vLay.addLayout(hlay4)
        vLay.addStretch(1)
        vLay.addLayout(hlay5)
        vLay.addStretch(1)

        self.widget.setLayout(vLay)

    def submit(self):
        try:
            x = Transaksi(self.cmbJenis.currentText(),
                          self.textTotal.text())

            kode = x.getTotalTransaksi()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
            msg.setInformativeText(f"Pemesanan berhasil, sisa saldo anda adalah {kode}")
            msg.setWindowTitle("Berhasil")
            s = msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()