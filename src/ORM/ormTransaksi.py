from sqlalchemy import Column, Date, Integer, String
from src.ORM.Base import Base, SessionFactory
from datetime import datetime


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

    # CRUD
    def insertTransaksi(self):
        try:
            session = SessionFactory()
            trsOrm = TransaksiOrm(self.getTanggalTransaksi(), self.getJenisTransaksi(),self.getTotalTransaksi())
            session.add(trsOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def readTransaksi():
        try:
            session = SessionFactory()
            for transaksi in session.query(TransaksiOrm).all():
                print("ID = {}, Tanggal = {}, Jenis Transaksi = {}, Total Transaksi = {}".format(transaksi.id, transaksi.tanggalTransaksi, transaksi.jenisTransaksi, transaksi.totalTransaksi))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updateTransaksi(x):
        try:
            dTotal = input("Masukkan Total Transaksi Baru: ")
            session = SessionFactory()
            session.query(TransaksiOrm).filter_by(id=x).update({
                TransaksiOrm.tanggalTransaksi: datetime.now().date(),
                TransaksiOrm.totalTransaksi: dTotal
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Update Berhasil")

    @staticmethod
    def deleteTransaksi(x):
        try:
            session = SessionFactory()
            session.query(TransaksiOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")
