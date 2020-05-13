from src.Class.Akun import Akun
from src.ORM.ormAkun import AdminOrm
from src.Class.Autentikasi import Autentikasi


class Admin(Akun, AdminOrm, Autentikasi):
    def tambahAkunPembeli(self):
        pass

    def tambahAkunPenjual(self):
        pass

    def tambahSaldoPembeli(self, obj, x):
        pass
