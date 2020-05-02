from sqlalchemy import Column, String, Integer, Enum
from src.Class.EnumClass import  JenisItem
from src.ORM.Base import Base, sessionFactory

class Menu(Base):
    __tablename__ = 'Menu'

    id = Column(Integer, primary_key=True)
    # namaPenjual = Column(String) NGAMBIL dari
    # menuItem = ISINYA SEHARUSNYA ARRAY YANG BERISI MENUITEMORM

class MenuItemOrm(Base):
    __tablename__ = 'MenuItem'

    id = Column(Integer, primary_key=True)
    namaItem = Column(String)
    jenisItem = Column(Enum(JenisItem))
    merekItem = Column(String)
    hargaItem = Column(Integer)
    kuantitasItem = Column(Integer)

    def __init__(self,namaItem, jenisItem,merekItem,hargaItem,kuantitasItem):
        self.namaItem = namaItem
        self.jenisItem = jenisItem
        self.merekItem = merekItem
        self.hargaItem = hargaItem
        self.kuantitasItem = kuantitasItem

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