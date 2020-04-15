class Pembeli():
    def __init__(self, id, nama, saldo, uang):
        self.__id = id
        self.__nama = nama
        self.__saldo = saldo
        self.__uang = uang

    # Getter & Setter
    def getId(self):
        return self.__id
    def setId(self, x):
        self.__id = x

    def getNama(self):
        return self.__nama
    def setNama(self, x):
        self.__nama = x

    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, x):
        self.__saldo = x

    def getUang(self):
        return self.__uang
    def setUang(self, x):
        self.__uang = x