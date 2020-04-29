from src.Class.EnumClass import JenisAkun

class Akun:
    def __init__(self,id,nama,jenisAkun):
        self.__id = id
        self.__nama = nama
        self.__jenisAkun = JenisAkun(jenisAkun)

    def getId(self):
        return self.__id
    def setId(self, x):
        self.__id = x
    def getNama(self):
        return self.__nama
    def setNama(self, x):
        self.__nama = x
    def getjenisAkun(self):
        return self.__jenisAkun.name
    def setjenisAkun(self, x):
        self.__jenisAkun = JenisAkun(x)