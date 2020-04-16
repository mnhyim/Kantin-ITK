import datetime

class Titipan:

    # Constructor
    def __init__(self, idBarang = None, namaPenitip = None, namaBarang = None, harga = None, jumlahTitipan = None, tanggal = None):
        self.__idBarang = idBarang
        self.__namaPenitip = namaPenitip
        self.__namaBarang = namaBarang
        self.__harga = harga
        self.__jumlahTitipan = jumlahTitipan
        self.__tanggal = tanggal
    
    # Getter dan Setter
    def getIdBarang(self):
        return self.__idBarang
    
    def setIdBarang(self, x):
        self.__idBarang = x
    
    def getNamPenitip(self):
        return self.__namaPenitip
    
    def setNamaPenitip(self, x):
        self.__namaPenitip = x

    def getNamaBarang(self):
        return self.__namaBarang
    
    def setNamaBarang(self, x):
        self.__namaBarang = x

    def getHarga(self):
        return self.__harga
    
    def setHarga(self, x):
        self.__harga = x

    def getJumlahTitipan(self):
        return self.__jumlahTitipan
    
    def setJumlahTitipan(self, x):
        self.__jumlahTitipan = x

    def getTanggal(self):
        return self.__tanggal
    
    def setTanggal(self, y, m, d):
        self.__tanggal = datetime.date(y, m, d)    
    
    
