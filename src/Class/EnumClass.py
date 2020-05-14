from enum import Enum


# ENUM


class JenisAkun(Enum):
    Admin = 1
    Penjual = 2
    Pembeli = 3


class JenisItem(Enum):
    BIASA = 1
    TITIPAN = 2

for i in JenisAkun:
    print(i)