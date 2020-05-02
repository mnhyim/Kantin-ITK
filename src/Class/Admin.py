from src.Class.Akun import Akun

class Admin(Akun):
    def __init__(self, id, nama, JenisAkun):
        super().__init__(id, nama, JenisAkun)

    def tambahAkunPembeli(self):
        pass
    def tambahAkunPenjual(self):
        pass
    def tambahSaldoPembeli(self, obj, x):
        obj.setSaldo(x)