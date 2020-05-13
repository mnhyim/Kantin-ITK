from src.Class.Admin import *
from src.Class.Penjual import *
from src.Class.Pembeli import *

a = Pembeli("Joko Purnomo","jokpur@gmail.com","jokcool",3,50000)
a.insert()
# a.read()
b = Penjual("Habib Rizik","bibrizik@gmail.com","bibib123",2,100000,"JEJE")
b.insert()
# b.read()
c = Admin("Hax","haxer@gm.com","hax123",1)
# c.login()
c.insert()
# c.read()