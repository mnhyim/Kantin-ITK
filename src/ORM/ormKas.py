from sqlalchemy import Column, Date, Integer
from src.ORM.Base import Base


class KasOrm(Base):
    __tablename__ = 'Data Kas'

    id = Column(Integer, primary_key=True)
    tanggalKas = Column(Date)
    pemasukan = Column(Integer)
    pengeluaran = Column(Integer)
    labaBersih = Column(Integer)

    def __init__(self, tanggalKas, pemasukan, pengeluaran, labaBersih):
        self.tanggalKas = tanggalKas
        self.pemasukan = pemasukan
        self.pengeluaran = pengeluaran
        self.labaBersih = labaBersih