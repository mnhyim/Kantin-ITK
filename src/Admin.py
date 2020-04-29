from base import sessionFactory
#from db.Orm.AdminOrm import AdminOrm
from SaldoOrm import SaldoOrm
from akun_pembeliOrm import akun_pembeliOrm
from akun_penjualOrm import akun_penjualOrm

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

    def set_user_saldo(self, username):
        self.user_saldo = username

    def get_user_saldo(self):
        return self.user_saldo

    def set_jumlah_saldo(self, username):
        self.jumlah_saldo = username

    def get_jumalah_saldo(self):
        return self.jumlah_saldo

    def set_username_pembeli(self, username):
        self.userpembeli = username
    
    def get_username_pembeli(self):
        retun self.userpembeli

    def set_username_pembeli(self, username):
        self.userpembeli = username
    
    def get_username_penjuak(self):
        retun self.userpenjual

    #Orm
    """
    def tambah_saldo(self, nama, user, saldo):
        try:
            session = sessionFactory()
            saldoOrm = SaldoOrm(nama, user, saldo)
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
            session.query(SaldoOrm).filter_by(user_saldo=username).update({
                SaldoOrm.username: newuserSaldo, 
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
                print("Nama = {}\nUsername = {}\nJumlah Saldo = {}\n====================".format(user.namaPembeli, user.username, user.jumlah_saldo))
            session.close()
        except Exception as e:
            print(">>>", e)
    """
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

    def update_akun_pembeli(self, idPembeli):
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

    def delete_akun_pembeli(self, idPembeli):
        try:
            session = sessionFactory()
            session.query(akun_pembeliOrm).filter_by(id=idPembeli).delete()
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Akun Berhasil Dihapus!")   

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

    def update_akun_penjual(self, idPenjual):
        try:
            newnamaPenjual = input("Masukkan Nama: ")
            newuserPenjual = input("Masukkan Username: ")
            newpassPenjual = input("Masukkan Password: ")
            session = sessionFactory()
            session.query(akun_penjualOrm).filter_by(id=idPenjual).update({
                akun_penjualOrm.namaPenjual : newnamaPenjual,
                akun_penjualOrm.username: newuserPenjual, 
                akun_penjualOrm.password: newpassPenjual}, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Akun Berhasil Diupdate!")  

    def delete_akun_penjual(self, idPenjual):
        try:
            session = sessionFactory()
            session.query(akun_penjualOrm).filter_by(id=idPenjual).delete()
            session.commit()
            session.close()
        except Exception as e:
            print(">>>", e)
        else:
            print("Akun Berhasil Dihapus!") 

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
a.tambah_akun_penjual("Andi","Maha","KKKK")
a.lihat_akun_penjual()
#a.delete_akun_pembeli(2)
#a.tambah_saldo("Amin","Amin13",1000)
#a.lihat_saldo()
    

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
