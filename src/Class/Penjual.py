from src.Class.Akun import Akun
from src.ORM.Base import sessionFactory
from src.ORM.ormAkun import PenjualOrm

class Penjual(Akun):
    def __init__(self, id, nama, JenisAkun, saldo):
        super().__init__(id, nama, JenisAkun)
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, x):
        self.__saldo = x

    #CRUD
    def insertPenjual(self):
        try:
            session = sessionFactory()
            penjOrm = PenjualOrm(self.getNama(), self.getjenisAkun(),self.getSaldo())
            session.add(penjOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def readPenjual():
        try:
            session = sessionFactory()
            for penjual in session.query(PenjualOrm).all():
                print("ID = {}, Nama = {}, Jenis Akun = {}, saldo = {}".format(penjual.id, penjual.nama, penjual.jenisAkun.name, penjual.saldo))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updatePenjual(x):
        try:
            dNama = input("Masukkan Nama Baru: ")
            dSaldo = input("Masukkan Saldo Baru: ")
            session = sessionFactory()
            session.query(PenjualOrm).filter_by(id=x).update({
                PenjualOrm.nama: dNama,
                PenjualOrm.saldo: dSaldo
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Update Berhasil")

    @staticmethod
    def deletePenjual(x):
        try:
            session = sessionFactory()
            session.query(PenjualOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")
"""
p = Penjual(1, "Andi", 2, 10000)
#p.insertPenjual()
p.updatePenjual(1)
p.readPenjual()
"""