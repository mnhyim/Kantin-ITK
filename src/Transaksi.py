class Transaksi():
    def __init__(self,id,tanggal,totalPembayaran):
        self.__id = id
        self.__tanggal = tanggal
        self.__totalPembayaran = totalPembayaran

    # Getter & Setter
    def getId(self):
        return self.__id
    def setId(self, x):
        self.__id = x

    def getTanggal(self):
        return self.__tanggal
    def setTanggal(self, x):
        self.__tanggal = x

    def getTotalPembayaran(self):
        return self.__totalPembayaran
    def setTotalPembayaran(self, x):
        self.__totalPembayaran = x

