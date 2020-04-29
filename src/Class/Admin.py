from src.Class.Akun import Akun
from src.ORM.Base import sessionFactory
from src.ORM.ormAkun import AdminOrm


class Admin(Akun):
    def __init__(self, id, nama, JenisAkun):
        super().__init__(id, nama, JenisAkun)

    def tambahAkunPembeli(self):
        pass
    def tambahAkunPenjual(self):
        pass
    def tambahSaldoPembeli(self, obj, x):
        obj.setSaldo(x)

    #CRUD
    def insertAdmin(self):
        try:
            session = sessionFactory()
            admOrm = AdminOrm(self.getNama(), self.getjenisAkun())
            session.add(admOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def readAdmin():
        try:
            session = sessionFactory()
            for admin in session.query(AdminOrm).all():
                print("ID = {}, Nama = {}, Jenis Akun = {}".format(admin.id, admin.nama, admin.jenisAkun.name))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updateAdmin(x):
        try:
            dNama = input("Masukkan Nama Baru: ")
            session = sessionFactory()
            session.query(AdminOrm).filter_by(id=x).update({
                AdminOrm.nama: dNama
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Update Berhasil")

    @staticmethod
    def deleteAdmin(x):
        try:
            session = sessionFactory()
            session.query(AdminOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")


   