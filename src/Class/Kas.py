from datetime import datetime

class DataKas:
    def __init__(self,id,pemasukan,pengeluaran):
        self.__id = id
        self.__tglKas = datetime.now().date()
        self.__pemasukan = pemasukan
        self.__pengeluaran = pengeluaran

    def getId(self):
        return self.__id
    def setId(self,x):
        self.__id = x
    def getTglKas(self):
        return self.__tglKas
    def setTglKas(self,dd,mm,yyyy):
        self.__tglKas = datetime(yyyy,mm,dd).date()
    def getPemasukan(self):
        return self.__pemasukan
    def setPemasukan(self, x):
        self.__pemasukan = x
    def getPengeluaran(self):
        return self.__pengeluaran
    def setPengeluaran(self, x):
        self.__pengeluaran = x
    def hitungLabaBersih(self):
        return self.__pemasukan - self.__pengeluaran