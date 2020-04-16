class penjual:
    def __init__(self):
        self._idpenjual = 0
        self._namapenjual = None
    def get_idpenjual(self):
        return self._idpenjual
    def set_idpenjual(self, x):
        self._idpenjual = x

    def get_namapenjual(self):
        return self._namapenjual
    def set_namapenjual(self, x):
        self._namapenjual = x


# pj = penjual()
# pj.set_idpenjual([1,2])
# pj.set_namapenjual(['mamak ica', 'ibu ida'])
#
# print(pj.get_idpenjual())
# print(pj.get_namapenjual())
