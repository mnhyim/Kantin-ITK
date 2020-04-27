from sqlalchemy import Column, String, Integer
from base import Base, sessionFactory


class akun_penjualOrm(Base):
    __tablename__ = 'akun_penjual'

    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)
    password = Column(Integer)

    def __init__(self, username, password):
        self.username = username
        self.password = password