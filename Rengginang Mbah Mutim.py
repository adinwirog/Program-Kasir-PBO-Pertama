import mysql.connector
import getpass
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
        self.a = a
        self.s = s
        self.cursor.execute("SELECT * FROM `operator kasir`")
        self.res = self.cursor.fetchall()
        for x in self.res:
            if x[3] == self.a and x[4] == self.s:
                return True
        return False

    def show(self):
        self.cursor.execute("SELECT * FROM `operator kasir`")
        self.res = self.cursor.fetchall()
        print("id \t nama operator \t\t\t NIK \t\t\t username \t\t password")
        print("================================================================")
        for x in self.res:
            print(x[0],"\t",x[1],"\t\t",x[2],"\t",x[3],"\t\t",x[4])
        print("================================================================")

    def insert(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.query = "INSERT INTO `operator kasir`(namaoperator, nik, usernamekasir, passwordkasir) VALUES('{}', '{}', '{}', '{}')".format(self.a,self.b,self.c,self.d)
        self.cursor.execute(self.query)
        self.con.commit()
        print("Data Berhasil Ditambahkan")

    def update(self):
        pass

    def delete(self):
        pass

class dataAdmin(Database):
    def validasipass(self,a,c):
        self.a = a
        self.c = c
        self.cursor.execute("SELECT * FROM `admin`")
        self.res = self.cursor.fetchone()
        if self.res[2] == self.a and self.res[3] == self.c:
            return True
        else:
            return False

    def validasi(self):
        self.cursor.execute("SELECT * FROM `admin`")
        self.res = self.cursor.fetchone()
        return self.res

    def show(self):
        self.cursor.execute("SELECT * FROM `admin`")
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

    def update(self):
        pass

class dataProduk(Database):
    def getHarga(self,a):
        self.a = a
        self.query = "SELECT hargabarang FROM `produk` WHERE idbarang = '{}' ".format(self.a)
        # self.tuple = (self.a)
        self.cursor.execute(self.query)
        # self.con.commit()
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
        print("id produk \t nama produk \t\t\t Harga")
        print("================================================================")
        for x in self.res:
            # print(x)
            print(x[0],"\t\t",x[1],"\t\t\t",x[2])
        print("================================================================")

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

class dataPembeli(Database):
    def show(self):
        self.cursor.execute("SELECT * FROM `pembeli`")
        self.res = self.cursor.fetchall()
        for x in self.res:
            print(x)

    def insert(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.query = "INSERT INTO pembeli(namapembeli, telepon, alamat) VALUES('{}', '{}', '{}')".format(self.a,self.b,self.c)
        self.cursor.execute(self.query)
        self.con.commit()
        print("Berhasil memasukkan data")

    def update(self):
        pass

    def delete(self):
        pass 

class dataTransaksi(Database):
    def show(self):
        self.cursor.execute("SELECT * FROM `transaksi`")
        self.res = self.cursor.fetchall()
        for x in self.res:
            print(x)

    def insert(self):
        pass

    def delete(self):
        pass

class Sistem:
    def otentifikasi(self):
        print("\n====== Selamat Datang Di Program Kasir Mbah Mutim ======")
        print("Pilih Menu")
        print("1. Login \n2. Signup \n3. Keluar ")
        masuk = str(input("Input Di sini => "))
        if masuk == str(1) :
            self.login()
        elif masuk == str(2):
            self.signup()
        elif masuk == str(3):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("Input salah. Coba input lagi")
            self.otentifikasi()

    def validasiAdmin(self):
        a = dataAdmin()
        if a.validasi() == None :
            print ("\n!!!!!! Peringatan !!!!!!")
            print ("Program Ini Tidak Mempunyai Admin.")
            print ("Anda Harus Sign up Menjadi Admin Terlebih Dahulu.")
            print ("1. Signup \n2. Keluar")
            masuk = str(input("Input Di sini => "))
            if masuk == str(1):
                self.signupAdmin()
            elif masuk == str(2):
                print("\n====== Terima Kasih Telah Menggunakan ======")
            else:
                print("Input salah, Coba lagi")
                self.validasiAdmin()
        else:
            self.otentifikasi()

    def login(self):
        print("\n=================")
        print("Login Sebagai Apa?")
        print("1. Admin \n2. Operator Kasir \n3. Menu Utama")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            self.masukAdmin()
        elif masuk == str(2):
            self.masukKasir()
        elif masuk == str(3):
            self.otentifikasi()
        else:
            print("Input salah, Coba lagi")
            self.login()

    def signup(self):
        a = dataAdmin()
        print("\n=================")
        print("Signup Sebagai Apa?")
        print("1. Admin \n2. Operator Kasir \n3. Menu Utama")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            if a.validasi() == None:
                self.signupAdmin()
            else:
                print("\nProgram Ini Sudah Memiliki Admin")
                self.signup()
        elif masuk == str(2):
            print("Masuk sign up kasir")
            self.signupKasir()
        elif masuk == str(3):
            self.otentifikasi()
        else:
            print("\nInput salah, Coba lagi")
            self.signup()

    def signupAdmin(self):
        a = dataAdmin()
        b = str(input("Masukkan Nama Admin=> "))
        c = str(input("Masukkan Username=> "))
        d = str(getpass.getpass("Masukkan Password=> "))
        a.insert(b,c,d)
        print("Selamat Anda Menjadi Admin")
        self.otentifikasi()

    def signupKasir(self):
        a = dataKasir()
        b = str(input("Masukkan Nama Anda=> "))
        c = str(input("Masukkan NIK Anda=> "))
        d = str(input("Masukkan Username=> "))
        e = str(getpass.getpass("Masukkan Password=> "))
        a.insert(b,c,d,e)
        print("Selamat Anda Terdaftar Menjadi Kasir")
        self.otentifikasi()

    def masukAdmin(self):
        w = dataAdmin()
        b = str(input("Masukkan username=> "))
        c = str(getpass.getpass("Masukkan Password=> "))
        i = 0
        if w.validasipass(b,c) == True:
            self.menuAdmin()
        else:
            print("\n!!!! Sepertinya Input Anda Salah. Coba Lagi!!!!!")
            while i<=3 and w.validasipass(b,c) == False:
                b = str(input("Masukkan username=> "))
                c = str(getpass.getpass("Masukkan Password=> "))
                if w.validasipass(b,c) == True:
                    self.menuAdmin()
                else:
                    i += 1 
                    if i > 3:
                        print()
                    else:
                        print("\n!!!! Coba Lagi !!!!!")
            if w.validasipass(b,c) == False:
                print("\n!!!! Sepertinya Anda Lupa Username Dan Password. Coba Ingat Terlebih Dahulu !!!!")
                print("\n!!!! Atau Lakukan Reset Akun Anda Di Database !!!!")

    def masukKasir(self):
        w = dataKasir()
        b = str(input("Masukkan username=> "))
        c = str(getpass.getpass("Masukkan Password=> "))
        i = 0
        if w.validasipass(b,c) == True:
            self.menuKasir()
        else:
            print("\n!!!! Sepertinya Input Anda Salah. Coba Lagi !!!!!")
            while i<=3 and w.validasipass(b,c) == False:
                b = str(input("Masukkan username=> "))
                c = str(getpass.getpass("Masukkan Password=> "))
                if w.validasipass(b,c) == True:
                    self.menuKasir()
                else:
                    i += 1 
                    if i > 3:
                        print()
                    else:
                        print("\n!!!! Coba Lagi !!!!!")
            if w.validasipass(b,c) == False:
                print("\n!!!!Sepertinya Anda Lupa Username Dan Password. Atau Anda Belum Terdaftar Di Program ini!!!!")
                print("\n!!!!Jika Anda Belum Terdaftar, Segera Sign Up Dan Hubungi Admin Program Ini!!!!")

    def menuAdmin(self):
        print("\n====== Menu Utama Admin ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Daftar Operator \n2. Daftar Produk \n3. Daftar Pembeli")
        print("4. Daftar Transaksi \n5. Recovery Admin \n6. Keluar")

    def menuKasir(self):
        print("\n====== Menu Utama Kasir ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Transaksi \n2. Lihat Daftar Produk \n3. Keluar")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            self.lakukanTransaksi()
        elif masuk == str(2):
            self.lihatProduk()
        elif masuk == str(3):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.menuKasir()

    def lakukanTransaksi(self):
        d1 = transaksiKasir()
        nama = str(input("Masukkan Nama Pembeli => "))
        nomor = str(input("Nomor Telepon Pembeli => "))
        alamat = str(input("Alamat Pembeli => "))
        d1.namaTransaksi(nama,nomor,alamat)
        print("\nIngin Membeli Produk Yang Mana?")

    
    def lihatProduk(self):
        a = dataProduk()
        a.show()
        print("Menu")
        print("\n1. Kembali Menu Utama")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            self.menuKasir()
        else:
            print("\nInput salah, Coba lagi\n")
            self.lihatProduk()


class transaksiKasir:
    def namaTransaksi(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        r = dataPembeli()
        r.insert(self.a,self.b,self.c)
        # self.nama = str(input("Input Di Sini => "))

    def doTransaksi(self):
        get = dataProduk()
        flag = False
        listProduk = []
        listKuantitas = []
        listHarga = []
        while flag == False:
            produk = str(input("Masukkan ID Produk Yang Ingin Dibeli => "))
            listProduk.append(produk)
            kuantitas = int(input("Jumlah yang ingin dipesan => "))
            listKuantitas.append(kuantitas)
            if produk == str(1):
                harga = kuantitas * get.getHarga(produk)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = str(input("\nMasukkan Input Di Sini => "))
                if masuk == str(1):
                    flag = False
                else:
                    flag = True
            elif produk == str(2):
                harga = kuantitas * get.getHarga(produk)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = str(input("\nMasukkan Input Di Sini => "))
                if masuk == str(1):
                    flag = False
                else:
                    flag = True
            elif produk == str(3):
                harga = kuantitas * get.getHarga(produk)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = str(input("\nMasukkan Input Di Sini => "))
                if masuk == str(1):
                    flag = False
                else:
                    flag = True
            elif produk == str(4):
                harga = kuantitas * get.getHarga(produk)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = str(input("\nMasukkan Input Di Sini => "))
                if masuk == str(1):
                    flag = False
                else:
                    flag = True
            elif produk == str(5):
                harga = kuantitas * get.getHarga(produk)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = str(input("\nMasukkan Input Di Sini => "))
                if masuk == str(1):
                    flag = False
                else:
                    flag = True
            elif produk == str(6):
                harga = kuantitas * get.getHarga(produk)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = str(input("\nMasukkan Input Di Sini => "))
                if masuk == str(1):
                    flag = False
                else:
                    flag = True
            elif produk == str(7):
                harga = kuantitas * get.getHarga(produk)
                listHarga.append(harga)
                print("\n Ingin Beli Lagi?\n")
                print("1. Ya \n2. Tidak")
                masuk = str(input("\nMasukkan Input Di Sini => "))
                if masuk == str(1):
                    flag = False
                else:
                    flag = True
            else:
                flag = True

        # tul = []
        
        for i in range(len(listProduk)):
            print(listProduk[i], listKuantitas[i], listHarga[i])
            # daftar = str(get.namaBarang(listProduk[i]))
            # tul.append(daftar)

        # tuples = tuple(tul)

        # print(tuples)
        
        # print ("Dengan Produk {}\n{}".format(tuples[0],tuples[1]))
        






p1 = transaksiKasir()
p1.doTransaksi()

