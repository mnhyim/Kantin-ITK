class Admin:
    def __init__(self, idAdmin = None, namaAdmin = None, saldo = None, userpembeli = None, userpembeli = None, pswdpembeli = None, userpenjual = None, pswdpenjual = None):
        self.idAdmin = idAdmin
        self.namaAdmin = namAdmin
        self.user_saldo = user 
        self.jumlah_saldo = 0
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

    def tambah_saldo(self,user,saldo):
        self.user_saldo = user
        self.jumlah_saldo = self.jumlah_saldo + saldo

    def lihat_user_saldo(self):
        return self.user_saldo

    def lihat_user_saldo(self):
        return self.jumlah_saldo
    
    def tambah_user_pembeli(self, user):
        self.userpembeli = user

    def lihat_user_pembeli(self):
        return self.userpembeli
        
    def tambah_pass_pembeli(self, pswd):
        self.pswdpembeli = pswd

    def lihat_pass_pembeli(self):
        return self.pswdpembeli

    def tambah_akun_penjual(self, user):
        self.userpenjual = user

    def lihat_user_penjual(self):
        return self.userpenjual
        
    def tambah_pass_penjual(self, pswd):
        self.pswdpenjual = pswd

    def lihat_pass_penjual(self):
        return self.pswdpenjual  
        

