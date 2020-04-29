from src.Class.Akun import Akun
from src.ORM.Base import sessionFactory
from src.ORM.ormAkun import PembeliOrm

class Pembeli(Akun):
    def __init__(self, id, nama, JenisAkun, saldo):
        super().__init__(id, nama, JenisAkun)
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, x):
        self.__saldo = x

    #CRUD
    def insertPembeli(self):
        try:
            session = sessionFactory()
            pembOrm = PembeliOrm(self.getNama(), self.getjenisAkun(),self.getSaldo())
            session.add(pembOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def readPembeli():
        try:
            session = sessionFactory()
            for pembeli in session.query(PembeliOrm).all():
                print("ID = {}, Nama = {}, Jenis Akun = {}, saldo = {}".format(pembeli.id, pembeli.nama, pembeli.jenisAkun.name, pembeli.saldo))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updatePembeli(x):
        try:
            dNama = input("Masukkan Nama Baru: ")
            dSaldo = input("Masukkan Saldo Baru: ")
            session = sessionFactory()
            session.query(PembeliOrm).filter_by(id=x).update({
                PembeliOrm.nama: dNama,
                PembeliOrm.saldo: dSaldo
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Update Berhasil")

    @staticmethod
    def deletePembeli(x):
        try:
            session = sessionFactory()
            session.query(PembeliOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")
"""
p = Pembeli(1, "Andi", 3, 100000)
p.insertPembeli()

#p.deletePembeli(4)
p.readPembeli()
"""