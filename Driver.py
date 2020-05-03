from src.Class.Admin import *
from src.Class.Penjual import *
from src.Class.Pembeli import *

a = Admin(1,'a',1)
b = Penjual(1,'b',2,5)
c = Pembeli(1,'c',3,5)
a.insertAdmin()
b.insertPenjual()
c.insertPembeli()