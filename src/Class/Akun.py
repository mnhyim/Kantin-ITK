from src.Class.EnumClass import JenisAkun


class Akun:
    def __init__(self, nama, email, password, jenisAkun):
        self.__nama = nama
        self.__email = email
        self.__password = password
        self.__jenisAkun = JenisAkun(jenisAkun)
        self.__statusLogin = False

    def getNama(self):
        return self.__nama

    def setNama(self, x):
        self.__nama = x

    def getEmail(self):
        return self.__email

    def setEmail(self, x):
        self.__email = x

    def getPassword(self):
        return self.__password

    def setPassword(self, x):
        self.__password = x

    def getJenisAkun(self):
        return self.__jenisAkun

    def setjenisAkun(self, x):
        self.__jenisAkun = JenisAkun(x)

    def getStatusLogin(self):
        return self.__statusLogin

    def setStatusLogin(self, x):
        self.__statusLogin = x
