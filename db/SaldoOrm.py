from sqlalchemy import Column, String, Integer
from base import Base, sessionFactory


class SaldoOrm(Base):
    __tablename__ = 'saldo'
    
    id = Column(Integer, primary_key=True)
    user_saldo = Column(String, unique= True)
    jumlah_saldo = Column(Integer)

    def __init__(self, user_saldo, jumlah_saldo):
        self.user_saldo = user_saldo
        self.jumlah_saldo = jumlah_saldo