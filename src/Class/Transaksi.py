from src.db.Base import sessionFactory
from datetime import datetime
from src.db.orm.ormTransaksi import TransaksiOrm

class Transaksi:
    def __init__(self,id,jenisTransaksi,totalTransaksi):
        self.__id = id
        self.__tanggalTransaksi = datetime.now().date()
        self.__totalTransaksi = totalTransaksi
        self.__jenisTransaksi = jenisTransaksi

    def getId(self):
        return self.__id

    def setId(self,x):
        self.__id = x

    def getTanggalTransaksi(self):
        return self.__tanggalTransaksi

    def setTanggalTransaksi(self,dd,mm,yyyy):
        self.__tanggalTransaksi = datetime(yyyy,mm,dd).date()

    def getJenisTransaksi(self):
        return self.__jenisTransaksi

    def setJenisTransaksi(self, x):
        self.__jenisTransaksi = x

    def getTotalTransaksi(self):
        return self.__totalTransaksi

    def setTotalTransaksi(self, x):
        self.__totalTransaksi = x

    # CRUD
    def insertTransaksi(self):
        try:
            session = sessionFactory()
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
            session = sessionFactory()
            for transaksi in session.query(TransaksiOrm).all():
                print("ID = {}, Tanggal = {}, Jenis Transaksi = {}, Total Transaksi = {}".format(transaksi.id, transaksi.tanggalTransaksi, transaksi.jenisTransaksi, transaksi.totalTransaksi))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updateTransaksi(x):
        try:
            dTotal = input("Masukkan Total Transaksi Baru: ")
            session = sessionFactory()
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
            session = sessionFactory()
            session.query(TransaksiOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")

class TransaksiCash(Transaksi):
    def hitungTransaksiTotal(self,totalTransaksi,totalSaldo):
        return totalSaldo - totalTransaksi
        
class TransaksiSaldo(Transaksi):
    def hitungTransaksiTotal(self, totalTransaksi, totalUang):
        return totalUang - totalTransaksi
