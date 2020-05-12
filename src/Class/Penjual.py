from src.Class.Akun import Akun
from src.ORM.Base import SessionFactory
from src.ORM.ormAkun import PenjualOrm


class Penjual(Akun, PenjualOrm):
    def __init__(self, id, nama, email, password, jenisAkun, saldo):
        super().__init__(id, nama, email, password, jenisAkun)
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, x):
        self.__saldo = x
