from src.ORM.Base import SessionFactory
from src.ORM.ormAkun import *

# class Autentikasi:
#     def login(self):
#         session = SessionFactory()
#         query = session.query(ormPembeli).filter_by(username=self.getUsername()).first()
#         try:
#             if query.username == self.getUsername() and query.password == self.getPassword():
#                 return self.setStts(True)
#         except AttributeError:
#             print('Username %s not found' % (self.getUsername()))
#             return self.setStts(False)
#
#     def logout(self):
#         self.setStts(False)
