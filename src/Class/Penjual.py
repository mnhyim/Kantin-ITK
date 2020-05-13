from src.Class.Akun import Akun
from src.ORM.Base import SessionFactory
from src.ORM.ormAkun import PenjualOrm


class Penjual(Akun):
    def __init__(self, nama, email, password, jenisAkun, saldo, menu):
        super().__init__(nama, email, password, jenisAkun)
        self.__saldo = saldo
        self.__menu = [menu]

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, x):
        self.__saldo = x

    def getMenu(self):
        return self.__menu

    def setMenu(self, x):
        self.__menu.append(x)
