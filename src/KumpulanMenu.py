from ItemMenu import im

class Kumpulan:
    def __init__(self):
        self._item = im.item

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, x):
        self._item = x
   
# km = Kumpulan()
# print(km.item)
