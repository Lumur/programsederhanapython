import os
import datetime
def daftarbuah():
    print(
        "======= DAFTAR NAMA-NAMA BUAH ======"
        "\n"
        "Nama Buah" "\t: Mangga\n"
        "Harga" "\t\t: Rp.20.000/Kg\n"
        "Berat" "\t\t: 500Gram/Buah\n"
        "======================\n"
        "Nama Buah" "\t: Manggis\n"
        "Harga" "\t\t: Rp.30.000/Kg\n"
        "Berat" "\t\t: 500Gram/Buah\n"
        "======================\n"
        "Nama Buah" "\t: Durian\n"
        "Harga" "\t\t: Rp.40.000/Kg\n"
        "Berat" "\t\t: 500Gram/Buah\n"
        "======================\n"
        "Nama Buah" "\t: Apel\n"
        "Harga" "\t\t: Rp.50.000/Kg\n"
        "Berat" "\t\t: 500Gram/Buah\n"
        "=======================\n"
    )
def pembelianbuah():
    Mangga = int(20000)
    Manggis = int(30000)
    Durian = int(40000)
    Apel = int(50000)
    Waktu = datetime.datetime.now()


    print(
        "DAFTAR NAMA-NAMA BUAH\n\n"
        "[1] MANGGA\n"
        "[2] MANGGIS\n"
        "[3] DURIAN\n"
        "[4] APEL\n"
    )
    NamaPembeli = input("Masukkan Nama Pembeli\t:")
    NamaBuah = input("Pilih Nama Buah\t:")
    Jumlah = input("Masukkan Jumlah /Kg\t:")
    # angka digunakan untuk convert string menjadi integer
    angka = int(Jumlah)
    if NamaBuah == "1":
        hasil=Mangga*angka
        os.system('clear')
        print(
            '============= RIWAYAT PEMBELIAN BARANG ===========\n'
            'Nama Pembeli'f'\t\t:{NamaPembeli}\n'
            'Nama Barang' '\t\t:Mangga\n'
            'Harga Barang /kg' '\t:20.000\n'
            'Jumlah Pembelian'f'\t:{Jumlah} Kg\n'
            'Total Harga' f'\t:Rp.{hasil},00\n'
            
            "\nPEMBAYARAN BERHASIL DILAKUKAN \nPADA TANGGAL",
            (Waktu.strftime("%w-%B-%Y")), f"\nSEJUMLAH Rp.{hasil},00 \n"
            '=================================================='
        )
    # untuk input teks ke txt

    elif NamaBuah == "2":
        hasil = Manggis * angka
        os.system('clear')
        print(
            '============= RIWAYAT PEMBELIAN BARANG ===========\n'
            'Nama Pembeli'f'\t\t:{NamaPembeli}\n'
            'Nama Barang' '\t\t:Manggis\n'
            'Harga Barang /kg' '\t:30.000\n'
            'Jumlah Pembelian'f'\t:{Jumlah} Kg\n'
            'Total Harga' f'\t:Rp.{hasil},00\n'
            
            "\nPEMBAYARAN BERHASIL DILAKUKAN \nPADA TANGGAL",
            (Waktu.strftime("%w-%B-%Y")), f"\nSEJUMLAH Rp.{hasil},00\n"
            '=================================================='
        )
    elif NamaBuah == "3":
        hasil = Durian * angka
        os.system('cls')
        print(
            '============= RIWAYAT PEMBELIAN BARANG ===========\n'
            'Nama Pembeli'f'\t\t:{NamaPembeli}\n'
            'Nama Barang' '\t\t:Durian\n'
            'Harga Barang /kg' '\t:40.000\n'
            'Jumlah Pembelian'f'\t:{Jumlah} Kg\n'
            'Total Harga' f'\t:Rp.{hasil},00\n'
            
            "\nPEMBAYARAN BERHASIL DILAKUKAN \nPADA TANGGAL",
            (Waktu.strftime("%w-%B-%Y")), f"\nSEJUMLAH Rp.{hasil},00\n"
            '=================================================='
        )
    elif NamaBuah == "4":
        hasil = Apel * angka
        os.system('clear')
        print(
            '============= RIWAYAT PEMBELIAN BARANG ===========\n'
            'Nama Pembeli'f'\t\t:{NamaPembeli}\n'
            'Nama Barang' '\t\t:Apel\n'
            'Harga Barang /kg' '\t:50.000\n'
            'Jumlah Pembelian'f'\t:{Jumlah} Kg\n'
            'Total Harga' f'\t:Rp.{hasil},00\n'
            
            "\nPEMBAYARAN BERHASIL DILAKUKAN \nPADA TANGGAL",
            (Waktu.strftime("%w-%B-%Y")), f"\nSEJUMLAH Rp.{hasil},00\n"
            '================================================='
        )
    else:
        print(
                '===========ERROR 400==========='
                'HARAP MASUKKAN DATA DENGAN BENAR'
            )



while True: 
    os.system('clear')
    print (
        "========Selamat Datang========\n"
        '[1] Daftar Barang \t'
        '\n[2] Pembelian Barang\t'
    )

    masukkan=input("\nPilih salah satu menu diatas \t:")
    if masukkan =='1':
        os.system('clear')
        daftarbuah()
        ulang=input("Balik Ke Halaman Menu? (Y/N)")
        if ulang ==  "N":
            break
        elif ulang == "Y":
            print(masukkan)   
        else:
            os.system('clear')
            print(
            "==================PEMBERITAHUAN=================\n"
            "Untuk Input Pemilihan Opsi (Y/N) \nHarap Gunakan Huruf Kapital\n"
            "================================================\n"
            )
    elif masukkan =='2':
        os.system('clear')
        pembelianbuah()
        ulang=input("Balik Ke Halaman Menu? (Y/N)")
        if ulang ==  "N":
            break
        elif ulang == "Y":
            print(masukkan)  
        else:
            os.system('clear')
            print(
            "==================PEMBERITAHUAN=================\n"
            "Untuk Input Pemilihan Opsi (Y/N) \nHarap Gunakan Huruf Kapital\n"
            "================================================\n"
            )
    else:
        os.system('clear')
        print(
            "================= ERROR 400 ================\n"
            "Maaf Nomor yang anda inputkan tidak tersedia\n"
            '================ Bad Request ===============\n'
            )
        ulang=input("Balik Ke Halaman Menu? (Y/N)")
        if ulang ==  "N":
            break
        elif ulang == "Y":
            print(masukkan)  
        else:
            os.system('clear')
            print(
            "==================PEMBERITAHUAN=================\n"
            "Untuk Input Pemilihan Opsi (Y/N) \nHarap Gunakan Huruf Kapital\n"
            "================================================\n"
            )


