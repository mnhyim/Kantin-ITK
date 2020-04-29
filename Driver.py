from src.Admin import Admin
from src.Penjual import Penjual
from src.Pembeli import Pembeli
from src.Kas import DataKas
from src.Transaksi import *
from src.Menu import *

# Admin
a = Admin(1,'XXX',1)
a.insertAdmin()
# a.insertAdmin()
# a.readAdmin(2)
# a.updateAdmin(2)
# a.readAdmin(2)
# a.deleteAdmin(1)
# a.readAdmin(2)

# Penjual
b = Penjual(1,'Joko',2,5000)
b.insertPenjual()
# b.insertPenjual()
# b.readPenjual(2)
# b.updatePenjual(2)
# b.readPenjual(2)
# b.deletePenjual(1)
# b.readPenjual(2)

# Pembeli
c = Pembeli(1,'Wididi',3,50000)
c.insertPembeli()
# c.insertPembeli()
# c.readPembeli(2)
# c.updatePembeli(2)
# c.readPembeli(2)
# c.deletePembeli(1)
# c.readPembeli(2)

# Data Kas
d = DataKas(1,10000,2000)
d.insertKas()
# d.readKas()
# d.updateKas()
# d.deleteKas()
# Transaksi
e = TransaksiSaldo(1,'Saldo',21412312)
e.insertTransaksi()
# e.readTransaksi(1)
# e.updateTransaksi(1)
# e.readTransaksi(1)

# Menu & MenuItem
f = MenuItem(1,'Susu Dancoww',1,'Dancow',2000,12)
# f.insertMenuItem()
# f.readMenuItem()
# f.updateMenuItem(1)
# f.deleteMenuItem(1)
# f.readMenuItem()
