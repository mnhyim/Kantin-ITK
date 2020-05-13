from src.ORM.Base import SessionFactory
from src.ORM.ormAkun import *


class Autentikasi:
    def __init__(self, emailLogin=0, passwordLogin=0):
        self.__statusLogin = False
        self.__roleLogin = 0
        self.__emailLogin = emailLogin
        self.__passwordLogin = passwordLogin

    def getStatusLogin(self):
        return self.__statusLogin

    def setStatusLogin(self, x):
        self.__statusLogin = x

    def getRoleLogin(self):
        return self.__roleLogin

    def setRoleLogin(self, x):
        self.__roleLogin = x

    def login(self):
        session = SessionFactory()
        query1 = session.query(AdminOrm).filter_by(email=self.__emailLogin).first()
        query2 = session.query(PenjualOrm).filter_by(email=self.__emailLogin).first()
        query3 = session.query(PembeliOrm).filter_by(email=self.__emailLogin).first()

        if query1 != None:
            if query1.email == self.__emailLogin and query1.password == self.__passwordLogin:
                self.__statusLogin = True
                self.__roleLogin = query1.jenisAkun
        elif query2 != None:
            if query2.email == self.__emailLogin and query2.password == self.__passwordLogin:
                self.__statusLogin = True
                self.__roleLogin = query2.jenisAkun
        elif query3 != None:
            if query3.email == self.__emailLogin and query3.password == self.__passwordLogin:
                self.__statusLogin = True
                self.__roleLogin = query3.jenisAkun
        else:
            print('Email %s not found' % (self.__emailLogin))
            self.__statusLogin = False
            print(self.__statusLogin)

    def logout(self):
        self.__statusLogin = False
