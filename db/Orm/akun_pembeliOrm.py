from sqlalchemy import Column, String, Integer
from db.base import Base, sessionFactory


class akun_pembeliOrm(Base):
    __tablename__ = 'akun_pembeli'

    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)
    password = Column(Integer)

    def __init__(self, username, password):
        self.username = username
        self.password = password
