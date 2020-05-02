from sqlalchemy import Column, Date, Integer
from src.ORM.Base import Base, sessionFactory


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

    # CRUD
    def insertKas(self):
        try:
            session = sessionFactory()
            kasOrm = KasOrm(self.getTglKas(), self.getPemasukan(), self.getPengeluaran(), self.hitungLabaBersih())
            session.add(kasOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def updateKas(id):
        try:
            newPemasukan = input("Masukkan Jumlah Pemasukan: ")
            newPengeluaran = input("Masukkan Jumlah Pengeluaran: ")
            session = sessionFactory()
            session.query(KasOrm).filter_by(id=id).update({
                KasOrm.pemasukan: newPemasukan,
                KasOrm.pengeluaran: newPengeluaran
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("-->", e)
        else:
            print("Update Berhasil")

    @staticmethod
    def deleteKas(id):
        try:
            session = sessionFactory()
            session.query(KasOrm).filter_by(id=id).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("-->", e)
        else:
            print("Hapus Berhasil")

    @staticmethod
    def readKas():
        try:
            session = sessionFactory()
            for item in session.query(KasOrm).all():
                print("Id Kas = {}\nTanggal = {}\nPemasukan = {}\nPengeluaran = {}\nLaba Bersih = {}\n".format(item.id,                                                                                       item.labaBersih))
        except Exception as e:
            print("-->", e)