from sqlalchemy import Column, String, Integer
from db.base import Base, sessionFactory


class akun_pembeliOrm(Base):
    __tablename__ = 'akun_pembeli'

    username = Column(String, unique=True)
    password = Column(String)
    idpembeli = Column(Integer, primary_key = True)
    nama_Pembeli = Column(String)

    def __init__(self, username, password,idpembeli,nama_pembeli):
        self.username = username
        self.password = password
        self.idpembeli = idpembeli
        self.nama_pembeli = nama_pembeli
