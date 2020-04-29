from enum import Enum

# ENUM
class JenisAkun(Enum):
    ADMIN = 1
    PENJUAL = 2
    PEMBELI = 3
class JenisItem(Enum):
    BIASA = 1
    TITIPAN = 2