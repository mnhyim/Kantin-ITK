class penjual:
    def __init__(self, idpenjual, namapenjual):
        self._idpenjual = idpenjual
        self._namapenjual = namapenjual

    @property
    def semua(self):
        return "id penjual : {} \nnamapenjual : {}".format(self._idpenjual,self._namapenjual)

    @property
    def idpenjual(self):
        return self._idpenjual

    @idpenjual.setter
    def idpenjual(self, x):
        self._idpenjual = x

    @property
    def namapenjual(self):
        return self._namapenjual

    @namapenjual.setter
    def namapenjual(self, x):
        self._namapenjual = x

# pj = penjual(1,"mamak ica")
# print(pj.semua)

