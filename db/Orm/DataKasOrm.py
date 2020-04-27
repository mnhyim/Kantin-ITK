from sqlalchemy import Column, Integer, Date
from db.base import Base, sessionFactory

class DataKasOrm(Base):
    __tablename__ = 'Data Kas'

    idKas = Column(Integer, primary_key=True)
    pemasukan = Column(Integer)
    pengeluaran = Column(Integer)
    tanggal = Column(Date)
    labaBersih = Column(Integer)

    def __init__(self, idKas, pemasukan, pengeluaran, tanggal, labaBersih):
        self.idKas = idKas
        self.pemasukan = pemasukan
        self.pengeluaran = pengeluaran
        self.tanggal = tanggal
        self.labaBersih = labaBersih
        
