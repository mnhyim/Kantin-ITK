from sqlalchemy import Column, String, Integer, Date
from db.base import Base, sessionFactory


class TitipanOrm(Base):
    __tablename__ = 'Barang'

    idBarang = Column(Integer, primary_key = True)
    namaPenitip = Column(String)
    namaBarang = Column(String)
    hargaBarang = Column(String)
    jumlahBarang = Column(Integer)
    tanggalPenitipan = Column(Date)

    def __init__(self,idBarang, namaPenitip, namaBarang, hargaBarang, jumlahBarang, tanggalPenitipan):
        self.idBarang = idBarang
        self.namaPenitip = namaPenitip
        self.namaBarang = namaBarang
        self.hargaBarang = hargaBarang
        self.jumlahBarang = jumlahBarang
        self.tanggalPenitipan = tanggalPenitipan

