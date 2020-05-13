from sqlalchemy import Column, String, Integer, Enum
from src.Class.EnumClass import JenisAkun
from src.ORM.Base import Base, SessionFactory


class AdminOrm(Base):
    __tablename__ = 'Admin'

    id = Column(Integer, primary_key=True)
    nama = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    jenisAkun = Column(Enum(JenisAkun), nullable=False)

    def __init__(self, nama, email, password, jenisAkun):
        self.nama = nama
        self.email = email
        self.password = password
        self.jenisAkun = jenisAkun

    # CRUD
    def insert(self):
        try:
            session = SessionFactory()
            session.add(AdminOrm(self.getNama(), self.getEmail(), self.getPassword(), self.getJenisAkun()))
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def read():
        try:
            session = SessionFactory()
            for admin in session.query(AdminOrm).all():
                print("ID = {}, Nama = {}, Email = {}, Password = {}, Jenis Akun = {}".format(admin.id, admin.nama,
                                                                                              admin.email,
                                                                                              admin.password,
                                                                                              admin.jenisAkun.name))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def update(x):
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
    def delete(x):
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
    nama = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    jenisAkun = Column(Enum(JenisAkun), nullable=False)
    saldo = Column(Integer, nullable=False)
    menu = Column(String)

    def __init__(self, nama, email, password, jenisAkun, saldo, menu):
        self.nama = nama
        self.email = email
        self.password = password
        self.jenisAkun = jenisAkun
        self.saldo = saldo
        self.menu = menu

    # CRUD
    def insert(self):
        try:
            session = SessionFactory()
            session.add(
                PenjualOrm(self.getNama(), self.getEmail(), self.getPassword(), self.getJenisAkun(), self.getSaldo(),
                           self.getMenu()))
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def read():
        try:
            session = SessionFactory()
            for penjual in session.query(PenjualOrm).all():
                print("ID = {}, Nama = {}, Email = {}, Password = {}, Jenis Akun = {}, saldo = {}, menu = {}".format(
                    penjual.id,
                    penjual.nama,
                    penjual.email,
                    penjual.password,
                    penjual.jenisAkun,
                    penjual.saldo,
                    penjual.menu))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def update(x):
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
    def delete(x):
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
    nama = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    jenisAkun = Column(Enum(JenisAkun), nullable=False)
    saldo = Column(Integer, nullable=False)

    def __init__(self, nama, email, password, jenisAkun, saldo):
        self.nama = nama
        self.email = email
        self.password = password
        self.jenisAkun = jenisAkun
        self.saldo = saldo

    # CRUD
    def insert(self):
        try:
            session = SessionFactory()
            session.add(
                PembeliOrm(self.getNama(), self.getEmail(), self.getPassword(), self.getJenisAkun(), self.getSaldo()))
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Insert Berhasil")

    @staticmethod
    def read():
        try:
            session = SessionFactory()
            for pembeli in session.query(PembeliOrm).all():
                print("ID = {}, Nama = {}, Email = {}, Password = {}, Jenis Akun = {}, saldo = {}".format(pembeli.id,
                                                                                                          pembeli.nama,
                                                                                                          pembeli.email,
                                                                                                          pembeli.password,
                                                                                                          pembeli.jenisAkun,
                                                                                                          pembeli.saldo))
        except Exception as e:
            print("Error -->", e)

    @staticmethod
    def update(x):
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
    def delete(x):
        try:
            session = SessionFactory()
            session.query(PembeliOrm).filter_by(id=x).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("Error -->", e)
        else:
            print("Delete Berhasil")
