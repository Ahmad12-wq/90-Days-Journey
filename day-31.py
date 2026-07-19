## Day 31 ##
# Looping List & Enumerate

siswa = {"Ahmad","Budi","Siti"}
for i,nama in enumerate (siswa, start =1) :
    print (f"{i}. {nama}")


## Mini Project

nama_mahasiswa = []
menu = "\nMenu\n\t1. Input Mahasiswa\n\t2. Cetak Daftar Hadir\n\t3. Cari Mahasiswa\n\t4. Keluar"

while True :
    print (menu)
    program = int(input("Pilih menu : "))
    if program == 1 :
        tambah_mahasiswa = input("Masukkan nama mahasiswa : ")
        nama_mahasiswa.append (tambah_mahasiswa)
    elif program == 2 :
        print("Daftar Hadir")
        for i, nama in enumerate(nama_mahasiswa, start = 1) :
            print (f"\t{i}. {nama}")
    elif program == 3 :
        cari_mahasiswa = input("Masukkan nama mahasiswa yang ingin dicari : ")
        if cari_mahasiswa in nama_mahasiswa :
            print(f"{cari_mahasiswa} terdaftar sebagai mahasiswa")
        else :
            print(f"{cari_mahasiswa} tidak terdaftar sebagai mahasiswa")
    elif program == 4 :
        break
