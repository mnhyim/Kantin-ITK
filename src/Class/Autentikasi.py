from src.ORM.Base import SessionFactory
from src.ORM.ormAkun import *


class Autentikasi:
    def __init__(self, emailLogin=0, passwordLogin=0):
        self.__statusLogin = False
        self.__emailLogin = emailLogin
        self.__passwordLogin = passwordLogin

    def getStatusLogin(self):
        return self.__statusLogin

    def setStatusLogin(self, x):
        self.__statusLogin = x

    def login(self):
        session = SessionFactory()
        query1 = session.query(AdminOrm).filter_by(email=self.__emailLogin).first()
        query2 = session.query(PenjualOrm).filter_by(email=self.__emailLogin).first()
        query3 = session.query(PembeliOrm).filter_by(email=self.__emailLogin).first()

        if query1 != None:
            if query1.email == self.__emailLogin and query1.password == self.__passwordLogin:
                print("1")
                self.__statusLogin = True
                print(self.__statusLogin)
        elif query2 != None:
            if query2.email == self.__emailLogin and query2.password == self.__passwordLogin:
                print("2")
                self.__statusLogin = True
                print(self.__statusLogin)
        elif query3 != None:
            if query3.email == self.__emailLogin and query3.password == self.__passwordLogin:
                print("3")
                self.__statusLogin = True
                print(self.__statusLogin)
        else:
            print('Email %s not found' % (self.__emailLogin))
            self.__statusLogin = False
            print(self.__statusLogin)

    def logout(self):
        self.__statusLogin = False
