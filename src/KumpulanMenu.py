from ItemMenu import itemMenu
import sys

class KumpulanMenu:
    def __init__(self):
        self._itemmenu = itemMenu.get_itemMenu()


    def get_itemmenu(self):
        return self._itemmenu
    def set_itemmenu(self, x):
        self._itemmenu = x

# km = KumpulanMenu()
# print(km.get_itemmenu())


