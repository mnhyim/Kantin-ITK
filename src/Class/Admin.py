from src.Class.Akun import Akun
from src.ORM.ormAkun import AdminOrm


class Admin(Akun, AdminOrm):
    def tambahAkunPembeli(self):
        pass

    def tambahAkunPenjual(self):
        pass

    def tambahSaldoPembeli(self, obj, x):
        pass
