from src.Class.Akun import Akun
from src.ORM.ormAkun import AdminOrm
class Admin(Akun, AdminOrm):
    def __init__(self, id, nama, JenisAkun):
        super().__init__(id, nama, JenisAkun)
    def tambahAkunPembeli(self):
        pass
    def tambahAkunPenjual(self):
        pass
    def tambahSaldoPembeli(self, obj, x):
        pass