from src.Class.Akun import Akun
from src.ORM.Base import sessionFactory
from src.ORM.ormAkun import PenjualOrm

class Penjual(Akun, PenjualOrm):
    def __init__(self, id, nama, JenisAkun, saldo):
        super().__init__(id, nama, JenisAkun)
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, x):
        self.__saldo = x