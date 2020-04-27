from db.base import sessionFactory
from db.Orm.ItemMenuOrm import ItemMenuOrm

class itemMenu:
    def __init__(self, idMenu, item, hargaitem):
        self._idMenu = idMenu
        self._item = item
        self._hargaitem = hargaitem

    @property
    def idMenu(self):
        return self._idMenu

    @idMenu.setter
    def idMenu(self, x):
        self._idMenu = x
    @property
    def item(self):
        return self._item
    @item.setter
    def item(self, x):
        self._item = x

    @property
    def hargaitem(self):
        return self._hargaitem
    @hargaitem.setter
    def hargaitem(self, x):
        self._hargaitem = x

    @property
    def semua(self):
        return "id Menu : {} \nItem Menu : {} \nharga item : {}".format(self._idMenu,self._item,self.hargaitem)

# im = itemMenu(1, ["Ayam bakar" ,"Rawon" ,"Esteh"], [15000,10000,3000])
# print(im.semua)
