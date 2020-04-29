from src.Class.JenisItem import JenisItem
from src.db.Base import sessionFactory
from src.db.orm.ormMenu import MenuItemOrm

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

    # CRUD
    def insertMenuItem(self,):
        try:
            session = sessionFactory()
            menuItemOrm = MenuItemOrm(self.getNamaItem(),self.getJenisItem(), self.getMerekItem(), self.getHargaItem(), self.getKuantitasItem())
            session.add(menuItemOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def readMenuItem():
        try:
            session = sessionFactory()
            for item in session.query(MenuItemOrm).all():
                print("ID = {},Nama Item = {}, Jenis Item = {}, Merek Item = {}, Harga Item = {}, Kuantitas Item = {}"
                      .format(item.id, item.namaItem, item.jenisItem.name, item.merekItem, item.hargaItem, item.kuantitasItem))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updateMenuItem(x):
        try:
            dNama = input("Masukkan Nama Baru: ")
            djenisItem = int(input("Masukkan Jenis Item Baru (1/2): "))
            dmerekItem = input("Masukkan Merek Item Baru: ")
            dhargaItem = input("Masukkan Harga Item Baru: ")
            dkuantitasItem = input("Masukkan Kuantitas Item Baru: ")

            session = sessionFactory()
            session.query(MenuItemOrm).filter_by(id=x).update({
                MenuItemOrm.namaItem: dNama,
                MenuItemOrm.jenisItem: JenisItem(djenisItem),
                MenuItemOrm.merekItem: dmerekItem,
                MenuItemOrm.hargaItem: dhargaItem,
                MenuItemOrm.kuantitasItem: dkuantitasItem
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Update Berhasil")

    @staticmethod
    def deleteMenuItem(x):
        try:
            session = sessionFactory()
            session.query(MenuItemOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")