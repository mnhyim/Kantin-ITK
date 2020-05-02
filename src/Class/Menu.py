from src.Class.EnumClass import JenisItem
from src.ORM.ormMenu import MenuItemOrm

class Menu:
    def __init__(self,id,namaPenjual,menuItem):
        self.__id = id
        self.__namaPenjual = namaPenjual
        self.__menuItem = menuItem

    def getId(self):
        return self.__id
    def setId(self,x):
        self.__id = x
    def getNamaPenjual(self):
        return self.__namaPenjual
    def setNamaPenjual(self, x):
        self.__namaPenjual = x
    def getMenuItem(self):
        return self.__menuItem
    def setMenuItem(self, x):
        self.__menuItem = x

class MenuItem:
    def __init__(self,id,namaItem,jenisItem,merekItem,hargaItem,kuantitasItem):
        self.__id = id
        self.__namaItem = namaItem
        self.__jenisItem = JenisItem(jenisItem)
        self.__merekItem = merekItem
        self.__hargaItem = hargaItem
        self.__kuantitasItem = kuantitasItem

    def getId(self):
        return self.__id
    def setId(self,x):
        self.__id = x
    def getNamaItem(self):
        return self.__namaItem
    def setNamaItem(self,x):
        self.__namaItem = x
    def getJenisItem(self):
        return self.__jenisItem.name
    def setJenisItem(self,x):
        self.__jenisItem = JenisItem(x)
    def getMerekItem(self):
        return self.__merekItem
    def setMerekItem(self,x):
        self.__merekItem = x
    def getHargaItem(self):
        return self.__hargaItem
    def setHargaItem(self,x):
        self.__hargaItem = x
    def getKuantitasItem(self):
        return self.__kuantitasItem
    def setKuantitasItem(self,x):
        self.__kuantitasItem = x