import mysql.connector
import getpass
import texttable as tt
from datetime import datetime

class Database:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="",database="pbo")
            self.cursor = self.con.cursor()
            # print("Koneksi berhasil")
        except mysql.connector.Error as e :
            print("Gagal terhubung ke : {}".format(e))

    def show(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

class dataKasir(Database):
    def validasipass(self, a, s):
        self.__a = a
        self.__s = s
        self.cursor.execute("SELECT * FROM `operator kasir`")
        self.__res = self.cursor.fetchall()
        for x in self.__res:
            if x[3] == self.__a and x[4] == self.__s:
                return True
        return False

    def cekidkasir(self,a):
        self.a = a
        self.query = "SELECT idoperator FROM `operator kasir` WHERE namaoperator = '{}' ".format(self.a)
        self.cursor.execute(self.query)
        self.__res = self.cursor.fetchone()
        return self.__res[0]

    def ceknamakasir(self, usernama, sandikasir):
        self.__usernama = usernama
        self.__sandikasir = sandikasir
        self.query = "SELECT namaoperator FROM `operator kasir` WHERE usernamekasir = '{}' AND passwordkasir = '{}' ".format(self.__usernama,self.__sandikasir)
        self.cursor.execute(self.query)
        self.__res = self.cursor.fetchone()
        return self.__res[0]

    def show(self):
        self.cursor.execute("SELECT idoperator,namaoperator,nik FROM `operator kasir`")
        self.res = self.cursor.fetchall()
        kasir = [[]]
        tab = tt.Texttable(0)
        for x in self.res:
            kasir.append([x[0],x[1],int(x[2])])
        tab.add_rows(kasir)
        tab.header(['ID Operator', 'Nama Operator', 'NIK'])
        tab.set_cols_align(['c','c','c'])
        tab.set_cols_dtype(['a','a','a'])
        print(tab.draw())

    def insert(self,a,b,c,d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.query = "INSERT INTO `operator kasir`(namaoperator, nik, usernamekasir, passwordkasir) VALUES('{}', '{}', '{}', '{}')".format(self.__a,self.__b,self.__c,self.__d)
        self.cursor.execute(self.query)
        self.con.commit()
        print("Data Berhasil Ditambahkan")

    def update(self):
        self.show()
        pilihid = str(input("\nPilih Id Operator => "))
        self.cursor.execute("SELECT idoperator,namaoperator,nik FROM `operator kasir` WHERE idoperator = '{}'".format(pilihid))
        self.__res = self.cursor.fetchone()
        print("\nId Operator \t\t= '{}' \nNama Operator \t\t= '{}' \nNIK \t\t= '{}'".format(self.res[0],self.res[1],self.res[2]))
        nama = str(input("\nMasukkan Nama Operator Baru => "))
        nik = str(input("\nMasukkan NIK Baru => "))
        self.query = "UPDATE `operator kasir` SET namaoperator = '{}', nik = '{}' WHERE idoperator = '{}'".format(nama,nik,pilihid)
        self.cursor.execute(self.query)
        self.con.commit()
        print("\nData Berhasil Diubah")

    def updatepass(self):
        self.show()
        pilihid = str(input("\nPilih Id Operator => "))
        self.cursor.execute("SELECT idoperator,namaoperator,nik FROM `operator kasir` WHERE idoperator = '{}'".format(pilihid))
        self.__res = self.cursor.fetchone()
        print("\nId Operator \t\t= '{}' \nNama Operator \t\t= '{}' \nNIK \t\t= '{}'".format(self.__res[0],self.__res[1],self.__res[2]))
        username = str(input("\nMasukkan Username Baru => "))
        password = str(getpass.getpass("\nMasukkan Password Baru => "))
        self.__query = "UPDATE `operator kasir` SET usernamekasir = '{}', passwordkasir = '{}' WHERE idoperator = '{}'".format(username,password,pilihid)
        self.cursor.execute(self.__query)
        self.con.commit()
        print("\nData Berhasil Diubah")

    def delete(self):
        self.show()
        pilihid = str(input("\nPilih Id Operator => "))
        self.query = "DELETE FROM `operator kasir` WHERE idoperator = '{}'".format(pilihid)
        self.cursor.execute(self.query)
        self.con.commit()
        print("\nData Berhasil Dihapus")

class dataAdmin(Database):
    def validasipass(self,a,c):
        self.__a = a
        self.__c = c
        self.cursor.execute("SELECT * FROM `admin`")
        self.__res = self.cursor.fetchone()
        if self.__res[2] == self.__a and self.__res[3] == self.__c:
            return True
        else:
            return False

    def validasi(self):
        self.cursor.execute("SELECT * FROM `admin`")
        self.__res = self.cursor.fetchone()
        return self.__res

    def show(self):
        self.cursor.execute("SELECT idadmin,namaadmin FROM `admin`")
        self.res = self.cursor.fetchone()
        print(self.res)

    def insert(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.query = "INSERT INTO admin(namaadmin, usernameadmin, passwordadmin) VALUES('{}', '{}', '{}')".format(self.a,self.b,self.c)
        self.cursor.execute(self.query)
        self.con.commit()
        print("Admin Telah Terdaftar")

    def updateakun(self):
        self.show()
        pilihid = str(input("\nPilih Id Admin => "))
        username = str(input("\nMasukkan Username Yang Baru => "))
        password = str(getpass.getpass("\nMasukkan Password Yang Baru => "))
        self.query = "UPDATE `admin` SET usernameadmin = '{}', password = '{}' WHERE idadmin = '{}'".format(username,password,pilihid)
        print("Data Berhasil Diubah")

class dataProduk(Database):
    def getHarga(self,a):
        self.a = a
        self.query = "SELECT hargabarang FROM `produk` WHERE idbarang = '{}' ".format(self.a)
        self.cursor.execute(self.query)
        self.res = self.cursor.fetchone()
        return int(self.res[0])

    def namaBarang(self,b):
        self.b = b
        self.query = "SELECT namabarang FROM `produk` WHERE idbarang = '{}' ".format(self.b)
        self.cursor.execute(self.query)
        self.res = self.cursor.fetchone()
        return self.res[0]

    def show(self):
        self.cursor.execute("SELECT * FROM `produk`")
        self.res = self.cursor.fetchall()
        tab = tt.Texttable()
        produk = [[]]
        for x in self.res:
            produk.append([x[0],x[1],x[2]])
        tab.add_rows(produk)
        tab.set_cols_align(['c','c','c'])
        tab.header(['ID Produk', 'Nama Produk', 'Harga'])
        print(tab.draw())

    def insert(self,a,b):
        self.a = a
        self.b = b
        self.query = "INSERT INTO `produk`(namabarang, hargabarang) VALUES('{}', '{}')".format(self.a,self.b)
        self.cursor.execute(self.query)
        self.con.commit()
        print("Data Berhasil Ditambahkan")

    def updateHarga(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        self.cursor.execute("SELECT idbarang,namabarang,hargabarang FROM `produk` WHERE idbarang = '{}'".format(pilihid))
        self.__res = self.cursor.fetchone()
        print("\nId Produk \t\t= '{}' \nNama Produk \t\t= '{}' \nHarga Produk \t\t= '{}'".format(self.__res[0],self.__res[1],self.__res[2]))
        harga = str(input("\nMasukkan Harga Baru => "))
        self.__query = "UPDATE `produk` SET hargabarang = '{}' WHERE idbarang = '{}'".format(harga,pilihid)
        self.cursor.execute(self.__query)
        self.con.commit()
        print("\nHarga Berhasil Diubah")

    def updateNama(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        self.cursor.execute("SELECT idbarang,namabarang,hargabarang FROM `produk` WHERE idbarang = '{}'".format(pilihid))
        self.res = self.cursor.fetchone()
        print("\nId Produk \t\t= '{}' \nNama Produk \t\t= '{}' \nHarga Produk \t\t= '{}'".format(self.res[0],self.res[1],self.res[2]))
        nama = str(input("\nMasukkan Nama Produk Baru => "))
        self.query = "UPDATE `produk` SET namabarang = '{}' WHERE idbarang = '{}'".format(nama,pilihid)
        self.cursor.execute(self.query)
        self.con.commit()
        print("\nNama Produk Berhasil Diubah")

    def updateall(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        self.cursor.execute("SELECT idbarang,namabarang,hargabarang FROM `produk` WHERE idbarang = '{}'".format(pilihid))
        self.__res = self.cursor.fetchone()
        print("\nId Produk \t\t= '{}' \nNama Produk \t\t= '{}' \nHarga Produk \t\t= '{}'".format(self.__res[0],self.__res[1],self.__res[2]))
        nama = str(input("\nMasukkan Nama Produk Baru => "))
        harga = str(input("\nMasukkan Harga Baru => "))
        self.__query = "UPDATE `produk` SET namabarang = '{}', hargabarang = '{}' WHERE idbarang = '{}'".format(nama,harga,pilihid)
        self.cursor.execute(self.__query)
        self.con.commit()
        print("\nData Produk Berhasil Diubah")

    def delete(self):
        self.show()
        pilihid = str(input("\nPilih Id Produk => "))
        self.__query = "DELETE FROM `produk` WHERE idbarang = '{}'".format(pilihid)
        self.cursor.execute(self.__query)
        self.con.commit()
        print("\nData Berhasil Dihapus")

class dataPembeli(Database):
    def cekPembelipass(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.query = "SELECT namapembeli FROM `pembeli` WHERE namapembeli = '{}' AND telepon = '{}' AND alamat = '{}' ".format(self.a,self.b,self.c)
        self.cursor.execute(self.query)
        self.res = self.cursor.fetchone()
        return self.res

    def cekid(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.query = "SELECT idpembeli FROM `pembeli` WHERE namapembeli = '{}' AND telepon = '{}' AND alamat = '{}' ".format(self.a,self.b,self.c)
        self.cursor.execute(self.query)
        self.res = self.cursor.fetchone()
        return self.res[0]

    def cekPembeli(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.query = "SELECT namapembeli FROM `pembeli` WHERE namapembeli = '{}' AND telepon = '{}' AND alamat = '{}' ".format(self.a,self.b,self.c)
        self.cursor.execute(self.query)
        self.res = self.cursor.fetchone()
        return self.res[0]

    def show(self):
        self.cursor.execute("SELECT * FROM `pembeli`")
        self.res = self.cursor.fetchall()
        tab = tt.Texttable()
        pembeli = [[]]
        for x in self.res:
            pembeli.append([x[0],x[1],x[2],x[3]])
        tab.add_rows(pembeli)
        tab.set_cols_align(['c','c','c','c'])
        tab.set_cols_dtype(['a','a','i','a'])
        tab.header(['ID Pembeli', 'Nama Pembeli', 'Telepon', 'Alamat'])
        print(tab.draw())

    def insert(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.query = "INSERT INTO pembeli(namapembeli, telepon, alamat) VALUES('{}', '{}', '{}')".format(self.__a,self.__b,self.__c)
        self.cursor.execute(self.__query)
        self.con.commit()
        print("Berhasil memasukkan data")

    def update(self):
        self.show()
        pilihid = str(input("\nPilih Id Pembeli => "))
        self.cursor.execute("SELECT idpembeli,namapembeli,telepon,alamat FROM `pembeli` WHERE idpembeli = '{}'".format(pilihid))
        self.__res = self.cursor.fetchone()
        print("\nId Pembeli \t\t= '{}' \nNama Pembeli \t\t= '{}' \nTelepon \t\t= '{}' \nAlamat \t\t= '{}'".format(self.__res[0],self.__res[1],self.__res[2],self.__res[3]))
        nama = str(input("\nMasukkan Nama Pembeli => "))
        telepon = str(input("\nMasukkan Nomor Telepon => "))
        alamat = str(input("\nMasukkan Alamat => "))
        self.__query = "UPDATE `pembeli` SET namapembeli = '{}', telepon = '{}', alamat = '{}' WHERE idpembeli = '{}'".format(nama,telepon,alamat,pilihid)
        self.cursor.execute(self.__query)
        self.con.commit()
        print("\nData Pembeli Berhasil Diubah")

    def delete(self):
        self.show()
        pilihid = str(input("\nPilih Id Pembeli => "))
        self.__query = "DELETE FROM `pembeli` WHERE idpembeli = '{}'".format(pilihid)
        self.cursor.execute(self.__query)
        self.con.commit()
        print("\nData Berhasil Dihapus")

class dataTransaksi(Database):
    def show(self):
        self.cursor.execute("SELECT namaoperator, namabarang, namapembeli, kuantitas, totalharga, tanggaltransaksi FROM transaksi JOIN pembeli ON pembeli.idpembeli = transaksi.idpembeli JOIN `operator kasir` ON `operator kasir`.`idoperator` = transaksi.idoperator JOIN produk ON produk.idbarang = transaksi.idbarang ORDER BY tanggaltransaksi DESC")
        self.res = self.cursor.fetchall()
        tab = tt.Texttable()
        transak = [[]]
        for x in self.res:
            transak.append([x[0],x[1],x[2],x[3],x[4],x[5]])
        tab.add_rows(transak)
        tab.set_cols_align(['c','c','c','c','c','c'])
        tab.header(['Nama Operator', 'Nama Barang', 'Nama Pembeli', 'Kuantitas', 'Total Harga', 'Tanggal'])
        print(tab.draw())

    def insert(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.query = "INSERT INTO transaksi(idoperator, idbarang, idpembeli, kuantitas, totalharga) VALUES('{}', '{}', '{}', '{}', '{}')".format(self.a,self.b,self.c,self.d,self.e)
        self.cursor.execute(self.query)
        self.con.commit()

    def delete(self):
        print("\nData Mulai Untuk Dihapus")
        self.cursor.execute("DELETE FROM `transaksi`")
        self.con.commit()
        print("\nData Berhasil Dihapus Semua")