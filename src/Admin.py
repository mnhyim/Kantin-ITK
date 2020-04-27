from base import sessionFactory
#from db.Orm.AdminOrm import AdminOrm
from db.Orm.SaldoOrm import SaldoOrm
from db.Orm.akun_pembeliOrm import akun_pembeliOrm
from db.Orm.akun_penjualOrm import akun_penjualOrm

class Admin:
    def __init__(self, idAdmin, namaAdmin, user_saldo=None, jumlah_saldo=None, userpembeli=None, pswdpembeli=None, userpenjual=None, pswdpenjual=None):
        self.idAdmin = idAdmin
        self.namaAdmin = namaAdmin
        self.user_saldo = user_saldo
        self.jumlah_saldo = jumlah_saldo
        self.userpembeli = userpembeli
        self.pswdpembeli = pswdpembeli
        self.userpenjual = userpenjual
        self.pswdpenjual = pswdpenjual
        
        
    #getter & setter
    def getId(self):
        return self.idAdmin
    
    def setId(self, Id):
        self.idAdmin = Id
    
    def getNama(self):
        return self.namaAdmin
    
    def setNama(self, Nama):
        self.namaAdmin = Nama

    def tambah_saldo(self, user, saldo):
        try:
            session = sessionFactory()
            saldoOrm = SaldoOrm(user, saldo)
            session.add(saldoOrm)
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Saldo Berhasil Disimpan!")
    
    def update_saldo(self, user_saldo):
        try:
            newuserSaldo = input("Masukkan Username: ")
            newjumlahSaldo = input("Masukkan Jumlah Saldo: ")
            session = sessionFactory()
            session.query(SaldoOrm).filter_by(user_saldo=user_saldo).update({
                SaldoOrm.user_saldo: newuserSaldo, 
                SaldoOrm.jumlah_saldo: newjumlahSaldo}, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Saldo Berhasil Diupdate!")

    def lihat_saldo(self):
        try:
            session = sessionFactory()
            for user in session.query(SaldoOrm).all():
                print("id = {}\nUsername = {}\nJumlah Saldo = {}\n===================="
                .format(user.id, user.user_saldo, user.jumlah_saldo))
            session.close()
        except Exception as e:
            print(">>>", e)
    
    def tambah_akun_pembeli(self, nama, username, password):
        try:
            session = sessionFactory()
            akunpembeliOrm = akun_pembeliOrm(nama, username, password)
            session.add(akunpembeliOrm)
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Akun Berhasil Disimpan!")

    def update_akun_pembeli(idPembeli):
        try:
            newnamaPembeli = input("Masukkan Nama: ")
            newuserPembeli = input("Masukkan Username: ")
            newpassPembeli = input("Masukkan Password: ")
            session = sessionFactory()
            session.query(akun_pembeliOrm).filter_by(id=idPembeli).update({
                akun_pembeliOrm.namaPembeli : newnamaPembeli,
                akun_pembeliOrm.username: newuserPembeli, 
                akun_pembeliOrm.password: newpassPembeli}, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Akun Berhasil Diupdate!")   

    def lihat_akun_pembeli(self):
        try:
            session = sessionFactory()
            for user in session.query(akun_pembeliOrm).all():
                print("Nama = {} \nUsername = {}\nPassword = {}\n====================".format(user.namaPembeli, user.username, user.password))
            session.close()
        except Exception as e:
            print(">>>", e)

    def tambah_akun_penjual(self, nama, username, password):
        try:
            session = sessionFactory()
            akunpenjualOrm = akun_penjualOrm(nama, username, password)
            session.add(akunpenjualOrm)
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Akun Berhasil Disimpan!")

    def update_akun_penjual(idPenjual):
        try:
            newnamaPenjual = input("Masukkan Nama: ")
            newuserPenjual = input("Masukkan Username: ")
            newpassPenjual = input("Masukkan Password: ")
            session = sessionFactory()
            session.query(akun_penjualOrm).filter_by(id=idPenjual).update({
                akun_pembeliOrm.namaPenjual : newnamaPenjual,
                akun_pembeliOrm.username: newuserPenjual, 
                akun_pembeliOrm.password: newpassPenjual}, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Akun Berhasil Diupdate!")   

    def lihat_akun_penjual(self):
        try:
            session = sessionFactory()
            for user in session.query(akun_penjualOrm).all():
                print("Nama = {} \nUsername = {}\nPassword = {}\n====================".format(user.namaPenjual, user.username, user.password))
            session.close()
        except Exception as e:
            print(">>>", e)
        

"""
a = Admin("1", "andi")
#a.tambah_saldo("marissa", 1000)
a.lihat_saldo()
    

a = Admin()
l = Login()

def main():
    while(True):
        print (l.getStatus())
        if l.getStatus() == "True":
            a.setId(input())
            a.setNama(input())
            print (a.getId())
            print (a.getNama())
            
        else:
            l.login_admin(input("Masukkan Username"),input("Masukkan Password"))
            
        
        
main()
"""
