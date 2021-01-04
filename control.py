from databaseku import*

class transaksiKasir:
    nama = ""
    telepon = ""
    alamat = ""
    namakasir = ""
    def namaTransaksi(self,a,b,c,d):
        self.nama = a
        self.telepon = b
        self.alamat = c
        self.namakasir = d
        r = dataPembeli()
        r.insert(self.nama,self.telepon,self.alamat)
        # self.nama = str(input("Input Di Sini => "))

    def tempNama(self,a,b,c,d):
        self.nama = a
        self.telepon = b
        self.alamat = c
        self.namakasir = d

    def doTransaksi(self):
        get = dataProduk()
        flag = False
        listProduk = []
        listKuantitas = []
        listHarga = []
        while flag == False:
            get.show()
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

        namaProduk = []
        totalHarga = 0
        kembalian = 0
        data1 = dataPembeli()
        data2 = dataKasir()
        data3 = dataTransaksi()
        idpembeli = data1.cekid(self.nama,self.telepon,self.alamat)
        idkasir = data2.cekidkasir(self.namakasir)

        for i in range(len(listProduk)):
            daftar = str(get.namaBarang(listProduk[i]))
            namaProduk.append(daftar)

        for i in range(len(listHarga)):
            totalHarga += listHarga[i]

        print("\nTotal Keseluruhan Harga Adalah => ", totalHarga)

        bayar = int(input("\nBerapa Uang Yang dibayar? => "))

        kembalian = bayar - totalHarga
        now = datetime.now()
        formatted_date = now.strftime('%d-%m-%Y %H:%M:%S')

        if kembalian >= 0 :
            print("\n================ STRUK PESANAN ====================")
            print("Tanggal Dan Waktu : ", formatted_date) 
            print("Atas Nama : ", self.nama)
            print("Alamat : ", self.alamat)
            print("Dengan Operator Kasir :", self.namakasir)
            print("Nama Produk \t|| Jumlah Pesanan || Jumlah Harga Per Pesan")
            print("--------------------------------------------------")
            for i in range(len(namaProduk)):
                print(namaProduk[i],"\t\t", listKuantitas[i],"\t\t", listHarga[i])
            print("--------------------------------------------------")
            print("Total Harga : \t\t\t\t", totalHarga)
            print("Kembalian : \t\t\t\t", kembalian)
            for i in range(len(listProduk)):
                data3.insert(idkasir,listProduk[i],idpembeli,listKuantitas[i],listHarga[i])
            print("\n1. OK")
            ok = str(input("\nMasukkan Input Di Sini => "))
        else:
            print("Maaf, Anda Tidak Bisa Melanjutkan Pembelian")


