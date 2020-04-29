from sqlalchemy import Column, String, Integer, Enum
from src.Class.JenisAkun import JenisAkun
from src.ORM.Base import Base

class AdminOrm(Base):
    __tablename__ = 'Admin'

    id = Column(Integer, primary_key=True)
    nama = Column(String)
    jenisAkun = Column(Enum(JenisAkun))

    def __init__(self,nama,jenisAkun):
        self.nama = nama
        self.jenisAkun = jenisAkun

class PenjualOrm(Base):
    __tablename__ = 'Penjual'
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    jenisAkun = Column(Enum(JenisAkun))
    saldo = Column(Integer)

    def __init__(self,nama,jenisAkun,saldo):
        self.nama = nama
        self.jenisAkun = jenisAkun
        self.saldo = saldo

class PembeliOrm(Base):
    __tablename__ = 'Pembeli'
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    jenisAkun = Column(Enum(JenisAkun))
    saldo = Column(Integer)

    def __init__(self,nama,jenisAkun,saldo):
        self.nama = nama
        self.jenisAkun = jenisAkun
        self.saldo = saldo