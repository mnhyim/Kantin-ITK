from sqlalchemy import Column, Date, Integer, String
from src.db.Base import Base


class TransaksiOrm(Base):
    __tablename__ = 'Data Transaksi'

    id = Column(Integer, primary_key=True)
    tanggalTransaksi = Column(Date)
    jenisTransaksi = Column(String)
    totalTransaksi = Column(Integer)

    def __init__(self, tanggalTransaksi, jenisTransaksi, totalTransaksi):
        self.tanggalTransaksi = tanggalTransaksi
        self.jenisTransaksi = jenisTransaksi
        self.totalTransaksi = totalTransaksi