from databaseku import *
from control import *
import getpass

class Sistem:
    namakasir = ""
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
        self.usernamekasir = str(input("Masukkan username=> "))
        self.passwordkasir = str(getpass.getpass("Masukkan Password=> "))
        i = 0
        if w.validasipass(self.usernamekasir,self.passwordkasir) == True:
            self.cekkasir(self.usernamekasir,self.passwordkasir)
        else:
            print("\n!!!! Sepertinya Input Anda Salah. Coba Lagi !!!!!")
            while i<=3 and w.validasipass(self.usernamekasir,self.passwordkasir) == False:
                self.usernamekasir = str(input("Masukkan username=> "))
                self.passwordkasir = str(getpass.getpass("Masukkan Password=> "))
                if w.validasipass(self.usernamekasir,self.passwordkasir) == True:
                    self.cekkasir(self.usernamekasir,self.passwordkasir)
                else:
                    i += 1 
                    if i > 3:
                        print()
                    else:
                        print("\n!!!! Coba Lagi !!!!!")
            if w.validasipass(self.usernamekasir,self.passwordkasir) == False:
                print("\n!!!!Sepertinya Anda Lupa Username Dan Password. Atau Anda Belum Terdaftar Di Program ini!!!!")
                print("\n!!!!Jika Anda Belum Terdaftar, Segera Sign Up Dan Hubungi Admin Program Ini!!!!")

    def cekkasir(self,a,b):
        self.a = a
        self.b = b
        f = dataKasir()
        self.namakasir = f.ceknamakasir(self.a,self.b)
        self.menuKasir(self.namakasir)

    def menuAdmin(self):
        print("\n====== Menu Utama Admin ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Menu Operator \n2. Daftar Produk \n3. Daftar Pembeli")
        print("4. Daftar Transaksi \n5. Recovery Admin \n6. Keluar")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            self.adminKasir()
        elif masuk == str(2):
            self.adminProduk()
        elif masuk == str(3):
            self.adminPembeli()
        elif masuk == str(4):
            self.adminTransaksi()
        elif masuk == str(5):
            self.recoverAdmin()
        elif masuk == str(6):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.menuAdmin()

    def adminKasir(self):
        k = dataKasir()
        print("\n====== Menu Manipulasi Operator ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Daftar Operator \n2. Tambah Data Operator \n3. Ubah Data Operator \n4. Hapus Data Operator")
        print("5. Main Menu \n6. Keluar")
        masuk = str(input("\nInput Di Sini => "))
        if masuk == str(1):
            k.show()
            ok = str(input("\nPress Any Input "))
            self.adminKasir()
        elif masuk == str(2):
            a = str(input("\nMasukkan Nama Kasir => "))
            b = str(input("\nMasukkan NIK => "))
            c = str(input("\nMasukkan Username Sementara => "))
            d = str(getpass.getpass("\nMasukkan Password Sementara => "))
            k.insert(a,b,c,d)
            k.show()
            ok = str(input("\nPress Any Input "))
            self.adminKasir()
        elif masuk == str(3):
            print("\nPilih Ubah Data")
            print("\n1. Ubah Biodata \n2. Reset Username Dan Password \n3. Return")
            pilihan = str(input("\nInput Di Sini => "))
            if pilihan == str(1):
                k.update()
                ok = str(input("\nPress Any Input "))
                self.adminKasir()
            elif pilihan == str(2):
                k.updatepass()
                ok = str(input("\nPress Any Input "))
                self.adminKasir()
            else:
                self.adminKasir()
        elif masuk == str(4):
            k.delete()
            ok = str(input("\nPress Any Input "))
            self.adminKasir()
        elif masuk == str(5):
            self.menuAdmin()
        elif masuk == str(6):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminKasir()

    def adminProduk(self):
        p = dataProduk()
        print("\n====== Menu Manipulasi Produk ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Daftar Produk \n2. Tambah Produk \n3. Ubah Data Produk \n4. Hapus Data Produk")
        print("5. Main Menu \n6. Keluar")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            p.show()
            ok = str(input("\nPress Any Input "))
            self.adminProduk()
        elif masuk == str(2):
            a = str(input("Masukkan Nama Produk => "))
            b = str(input("Masukkan Harga Per Buah => "))
            p.insert(a,b)
            p.show()
            ok = str(input("\nPress Any Input "))
            self.adminProduk()
        elif masuk == str(3):
            p.updateall()
            ok = str(input("\nPress Any Input "))
            self.adminProduk()
        elif masuk == str(4):
            p.delete()
            self.adminProduk()
        elif masuk == str(5):
            self.menuAdmin()
        elif masuk == str(6):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminProduk()

    def adminPembeli(self):
        c = dataPembeli()
        print("\n====== Menu Manipulasi Pembeli ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Daftar Pembeli \n2. Hapus Data Pembeli \n3. Ubah Data Pembeli")
        print("4. Main Menu \n5. Keluar")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            c.show()
            ok = str(input("\nPress Any Input "))
            self.adminPembeli()
        elif masuk == str(2):
            c.delete()
            ok = str(input("\nPress Any Input "))
            self.adminPembeli()
        elif masuk == str(3):
            c.update()
            ok = str(input("\nPress Any Input "))
            self.adminPembeli()
        elif masuk == str(4):
            self.menuAdmin()
        elif masuk == str(5):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminPembeli()

    def adminTransaksi(self):
        t = dataTransaksi()
        print("\n====== Menu Manipulasi Pembeli ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Lihat Riwayat Transaksi")
        print("3. Main Menu \n4. Keluar")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            t.show()
            ok = str(input("\nPress Any Input "))
            self.adminTransaksi()
        elif masuk == str(2):
            print("\nData Akan Dihapus Semua. Anda Yakin?")
            print("\n1. Ya \n2. Tidak")
            pilih = str(input("\nInput Di Sini => "))
            if pilih == str(1):
                t.delete()
                ok = str(input("\nPress Any Input "))
                self.adminTransaksi
            else:
                self.adminTransaksi
        elif masuk == str(3):
            self.menuAdmin()
        elif masuk == str(4):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.adminTransaksi()

    def recoverAdmin(self):
        m = dataAdmin()
        print("\nReset Akun Admin?")
        print("1. Ya \n2. Tidak")
        masuk = str(input("\n Input Di Sini => "))
        if masuk == str(1):
            m.updateakun()
            ok = str(input("\nPress Any Input "))
            self.menuAdmin()
        else:
            self.menuAdmin

    def menuKasir(self,a):
        self.a = a
        print("\n====== Menu Utama Kasir ======")
        print("\nPilih Menu Di Sini\n")
        print("1. Transaksi \n2. Lihat Daftar Produk \n3. Keluar")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            self.lakukanTransaksi(self.a)
        elif masuk == str(2):
            self.lihatProduk(self.a)
        elif masuk == str(3):
            print("\n====== Terima Kasih Telah Menggunakan ======")
        else:
            print("\nInput salah, Coba lagi")
            self.menuKasir(self.a)

    def lakukanTransaksi(self,a):
        self.a = a
        d1 = transaksiKasir()
        d2 = dataPembeli()
        nama = str(input("\nMasukkan Nama Pembeli => "))
        nomor = str(input("\nNomor Telepon Pembeli => "))
        alamat = str(input("\nAlamat Pembeli => "))
        print(d2.cekPembelipass(nama,nomor,alamat))
        if d2.cekPembelipass(nama,nomor,alamat) == None:
            d1.namaTransaksi(nama,nomor,alamat,self.a)
            d1.doTransaksi()
        else:
            d1.tempNama(nama,nomor,alamat,self.a)
            d1.doTransaksi()
        self.menuKasir(self.a)
    
    def lihatProduk(self,a):
        self.a = a
        b = dataProduk()
        b.show()
        print("Menu")
        print("\n1. Kembali Menu Utama")
        masuk = str(input("Input Di Sini => "))
        if masuk == str(1):
            self.menuKasir(self.a)
        else:
            print("\nInput salah, Coba lagi\n")
            self.lihatProduk(self.a)

p1 = Sistem()
p1.validasiAdmin()