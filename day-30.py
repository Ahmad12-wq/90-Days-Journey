## WEEK 5 : LIST ##
#DAY - 30 : MANIPULASI LIST

# PROGRAM ABSEN MAHASISWA #
menu = "Selamat datang di program absensi mahasiswa\nBerikut program yang bisa dilakukan disini :\n\t1. Tambah mahasiswa\n\t2. Hapus mahasiswa\n\t3. Ganti nama mahasiswa\n\t4. Selesai"
mahasiswa = []
while True : 
    print(menu)
    program = int(input("Masukkan program yang anda inginkan : "))
    if program == 1 :
        tambah_mahasiswa = input("Masukkan nama mahasiswa yang ingin ditambah : ")
        mahasiswa.append(tambah_mahasiswa)
    elif program == 2 :
        hapus_mahasiswa = input("Masukkan nama mahasiswa yang ingin dihapus : ")
        mahasiswa.remove(hapus_mahasiswa)
    elif program == 3 :
        ganti_nama = input("Masukkan nama mahasiswa yang akan diganti : ")
        nama_baru = input("Masukkan nama pengganti : ")
        i = mahasiswa.index(ganti_nama)
        mahasiswa[i] = nama_baru
    elif program == 4 :
        break
    print("\n",mahasiswa)


# Mini Project
# Aplikasi Daftar Belanja Sederhana

menu = "Selamat datang di aplikasi daftar belanja\nSilahkan pilih layanan :\n\t1. Tambah Barang\n\t2. Hapus Barang\n\t3.Lihat Daftar Barang\n\t4. Cek Barang\n\t5. Keluar"
daftar_belanjaan = []
while True :
    print("\n",menu)
    layanan = int(input("Masukkan nomor layanan yang anda inginkan : "))
    if layanan ==1:
        tambah_barang = input("Masukkan nama barang belanjaan : ")
        daftar_belanjaan.append(tambah_barang)
    elif layanan ==2 :
        hapus_barang = input("Masukkan barang yang akan dihapus : ")
    elif layanan==3:
        print(daftar_belanjaan)
    elif layanan==4:
        cek_barang = input("Masukkan nama barang yang ingin di-cek : ")
        if cek_barang in daftar_belanjaan :
            print (f"{cek_barang} sudah ada di belanjaan mu")
        else:
            print(f"{cek_barang} belum ada di belanjaan mu")
    elif layanan==5:
        break
    iflanjut=input("Lanjut belanja? (y/n) : ")

    if iflanjut == "n" :
        break
total_belanja = len(daftar_belanjaan)
print(f"Total belanjaan anda ada {total_belanja} item, dengan rincian {daftar_belanjaan}")




    

