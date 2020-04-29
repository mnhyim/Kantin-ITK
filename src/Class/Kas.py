from datetime import datetime
from src.db.Base import sessionFactory
from src.db.orm.ormKas import KasOrm

class DataKas:
    def __init__(self,id,pemasukan,pengeluaran):
        self.__id = id
        self.__tglKas = datetime.now().date()
        self.__pemasukan = pemasukan
        self.__pengeluaran = pengeluaran

    def getId(self):
        return self.__id

    def setId(self,x):
        self.__id = x

    def getTglKas(self):
        return self.__tglKas

    def setTglKas(self,dd,mm,yyyy):
        self.__tglKas = datetime(yyyy,mm,dd).date()

    def getPemasukan(self):
        return self.__pemasukan

    def setPemasukan(self, x):
        self.__pemasukan = x

    def getPengeluaran(self):
        return self.__pengeluaran

    def setPengeluaran(self, x):
        self.__pengeluaran = x

    def hitungLabaBersih(self):
        return self.__pemasukan - self.__pengeluaran

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
            session.query(KasOrm).filter_by(id = id).update({
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
    def hapusKas(id):
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
    def showKas():
        try:
            session = sessionFactory()
            for item in session.query(KasOrm).all():
                print("Id Kas = {}\nTanggal = {}\nPemasukan = {}\nPengeluaran = {}\nLaba Bersih = {}\n".format(item.id, item.tanggalKas, item.pemasukan, item.pengeluaran, item.labaBersih))
        except Exception as e:
            print("-->", e)

a = DataKas(1, 500000, 200000)
# a.insertKas()
# a.updateKas(1)
# a.hapusKas(1)
a.showKas()
