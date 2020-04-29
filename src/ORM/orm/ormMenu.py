from sqlalchemy import Column, String, Integer, Enum
from src.Class.JenisItem import JenisItem
from src.db.Base import Base

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