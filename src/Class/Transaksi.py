from datetime import datetime


class Transaksi:
    def __init__(self, jenisTransaksi, totalTransaksi):
        self.__tanggalTransaksi = datetime.now().date()
        self.__totalTransaksi = totalTransaksi
        self.__jenisTransaksi = jenisTransaksi

    def getTanggalTransaksi(self):
        return self.__tanggalTransaksi

    def setTanggalTransaksi(self, dd, mm, yyyy):
        self.__tanggalTransaksi = datetime(yyyy, mm, dd).date()

    def getJenisTransaksi(self):
        return self.__jenisTransaksi

    def setJenisTransaksi(self, x):
        self.__jenisTransaksi = x

    def getTotalTransaksi(self):
        return self.__totalTransaksi

    def setTotalTransaksi(self, x):
        self.__totalTransaksi = x


class TransaksiCash(Transaksi):
    def hitungTransaksiTotal(self, totalTransaksi, totalSaldo):
        return totalSaldo - totalTransaksi


class TransaksiSaldo(Transaksi):
    def hitungTransaksiTotal(self, totalTransaksi, totalUang):
        return totalUang - totalTransaksi
