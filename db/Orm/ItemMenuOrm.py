from sqlalchemy import Column, String, Integer, Date
from db.base import Base, sessionFactory


class TitipanOrm(Base):
    __tablename__ = 'Item Menu'

    idMenu = Column(Integer, primary_key = True)
    item = Column(String)
    hargaitem = Column(Integer)
    

    def __init__(self, idMenu, item, hargaitem):
        self._idMenu = idMenu
        self._item = item
        self._hargaitem = hargaitem
