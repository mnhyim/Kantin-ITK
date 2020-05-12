from sqlalchemy import Column, String, Integer, Enum
from src.Class.EnumClass import JenisAkun
from src.ORM.Base import Base, SessionFactory


class AdminOrm(Base):
    __tablename__ = 'Admin'

    id = Column(Integer, primary_key=True)
    nama = Column(String)
    email = Column(String)
    jenisAkun = Column(Enum(JenisAkun))

    def __init__(self, nama, email, jenisAkun):
        self.nama = nama
        self.email = email
        self.jenisAkun = jenisAkun

    # CRUD
    def insertAdmin(self):
        try:
            session = SessionFactory()
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
            session = SessionFactory()
            for admin in session.query(AdminOrm).all():
                print("ID = {}, Nama = {}, Jenis Akun = {}".format(admin.id, admin.nama, admin.jenisAkun.name))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updateAdmin(x):
        try:
            dNama = input("Masukkan Nama Baru: ")
            session = SessionFactory()
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
            session = SessionFactory()
            session.query(AdminOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")


class PenjualOrm(Base):
    __tablename__ = 'Penjual'
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    jenisAkun = Column(Enum(JenisAkun))
    saldo = Column(Integer)

    def __init__(self, nama, jenisAkun, saldo):
        self.nama = nama
        self.jenisAkun = jenisAkun
        self.saldo = saldo

    # CRUD
    def insertPenjual(self):
        try:
            session = SessionFactory()
            penjOrm = PenjualOrm(self.getNama(), self.getjenisAkun(), self.getSaldo())
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
            session = SessionFactory()
            for penjual in session.query(PenjualOrm).all():
                print("ID = {}, Nama = {}, Jenis Akun = {}, saldo = {}".format(penjual.id, penjual.nama,
                                                                               penjual.jenisAkun.name, penjual.saldo))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updatePenjual(x):
        try:
            dNama = input("Masukkan Nama Baru: ")
            dSaldo = input("Masukkan Saldo Baru: ")
            session = SessionFactory()
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
            session = SessionFactory()
            session.query(PenjualOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")


class PembeliOrm(Base):
    __tablename__ = 'Pembeli'
    id = Column(Integer, primary_key=True)
    nama = Column(String)
    jenisAkun = Column(Enum(JenisAkun))
    saldo = Column(Integer)

    def __init__(self, nama, jenisAkun, saldo):
        self.nama = nama
        self.jenisAkun = jenisAkun
        self.saldo = saldo

    # CRUD
    def insertPembeli(self):
        try:
            session = SessionFactory()
            pembOrm = PembeliOrm(self.getNama(), self.getjenisAkun(), self.getSaldo())
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
            session = SessionFactory()
            for pembeli in session.query(PembeliOrm).all():
                print("ID = {}, Nama = {}, Jenis Akun = {}, saldo = {}".format(pembeli.id, pembeli.nama,
                                                                               pembeli.jenisAkun.name, pembeli.saldo))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def updatePembeli(x):
        try:
            dNama = input("Masukkan Nama Baru: ")
            dSaldo = input("Masukkan Saldo Baru: ")
            session = SessionFactory()
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
            session = SessionFactory()
            session.query(PembeliOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")
