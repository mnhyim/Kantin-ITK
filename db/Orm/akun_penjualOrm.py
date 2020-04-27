from sqlalchemy import Column, String, Integer
from db.base import Base, sessionFactory


class akun_pembeliOrm(Base):
    __tablename__ = 'akun_penjual'

    username = Column(String, unique=True)
    password = Column(String)
    idpenjual = Column(Integer, primary_key = True)
    nama_penjual = Column(String)

    def __init__(self, username, password,idpenjual,nama_penjual):
        self.username = username
        self.password = password
        self.idpembeli = idpenjual
        self.nama_pembeli = nama_penjual
