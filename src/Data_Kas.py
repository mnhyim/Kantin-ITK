import datetime

class DataKas:
    
    # Constructor
    def __init__(self, idKas = None, tanggal = None, pemasukan = None, pengeluaran = None, labaBersih = None):
        self.__idKas = idKas
        self.__tanggal = tanggal
        self.__pemasukan = pemasukan
        self.__pengeluaran = pengeluaran
        self.__labaBersih = labaBersih

    # Getter dan Setter
    def getIdKas(self):
        return self.__idKas
    
    def setIdKas(self, x):
        self.__idKas = x
    
    def getTanggal(self):
        return self.__tanggal
    
    def setTanggal(self, y, m, d):
        self.__tanggal = datetime.date(y, m, d)

    def getPemasukan(self):
        return self.__pemasukan
    
    def setPemasukan(self, x):
        self.__pemasukan = x

    def getPengeluaran(self):
        return self.__pengeluaran
    
    def setPengeluaran(self, x):
        self.__pengeluaran = x
    
    def getLabaBersih(self):
        return self.__labaBersih
    
    def setLabaBersih(self):
        self.__labaBersih = self.__pemasukan - self.__pengeluaran