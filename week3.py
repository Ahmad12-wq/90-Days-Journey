#### Hari ke-15 ####

#Pengenalan If

# umur = int(input("Masukkan umur : "))
# saldo = int(input("Masukkan saldo : "))
# nilai = int(input("Masukkan nilai : "))

# if umur > 17 :
#     print ("Anda sudah dewasa, sudah bisa buat ktp")
# else :
#     kurang_umur = int(17 - umur)
#     print (f"Anda belum cukup umur, tunggu {kurang_umur} tahun lagi baru bisa buat ktp")

# if saldo >= 50000 :
#     sisa_saldo = saldo - 50000
#     print (f"Pembayaran diterima, sisa saldo anda tinggal Rp{sisa_saldo:,.0f}")
# else : 
#     kurang_saldo = 50000 - saldo
#     print (f"Saldo tidak mencukupi, uang anda kurang Rp{kurang_saldo:,.0f}")

# if nilai > 80 :
#     print ("Anda lulus tahap pertama, jangan lupa persiapkan berkas - berkas untuk tahap kedua minggu depan")
# else : 
#     print("Maaf, anda tidak lulus")


#### Hari ke- 16 ####
## If Else

# # Program Ganjil Genap
# angka = int(input("Masukkan angka : "))
# if angka % 2 == 0 :
#     print(f"{angka}, adalah angka genap")
# else :
#     print (f"{angka}, adalah angka ganjil")

# # Program Pengecekan Password
# password = input("Masukkan Password : ")
# if password == "anaksoleh123" :
#     print("Login berhasil")
# else : 
#     print ("Password salah, coba lagi")


#### Hari ke- 17 ####
## If Elif Else

# # Program Klasifikasi Umur
# umur = int(input("Masukkan Umur : "))

# if umur >= 0 and umur <= 5 :
#     print ("Anda termasuk dalam kategori balita, banyak banyak minum susu")
# elif umur > 5 and umur <= 11 :
#     print ("Anda termasuk dalam kategori kanak kanak, banyak banyak makan sayur")
# elif umur > 11 and umur <= 25 :
#     print ("Anda termasuk dalam kategori remaja, olahraga teratur biar tua masih sehat")
# elif umur > 25 and umur <= 45 :
#     print ("Anda termasuk dalam kategori dewasa, jangan lupa bahagia")
# else : 
#     print ("Anda termasuk dalam kategori lansia, jangan lupa bahagia")

# # Program Klasifikasi Tinggi Badan
# tinggi = int(input("Masukkan tinggi badan anda : "))

# if tinggi < 150 :
#     print("Kamu pendek")
# elif tinggi >= 150 and tinggi <= 170 :
#     print ("Kamu lumayan tinggi juga")
# elif tinggi > 170 :
#     print ("Kamu tinggi banget")


#### Hari ke- 18 ####
## If Bertingkat

# # Program Simulasi Login
# username = input("Masukkan username : ")
# password = input("Masukkan password : ")

# if username == "paijo123" :
#     if password == "ganteng123" :
#         print("Login berhasil")
#     else :
#         print ("Password salah, coba lagi")
# elif username == "siti123" :
#     if password == "cantik123" :
#         print ("Login berhasil")
#     else :
#         print ("Password salah, coba lagi")
# else :
#     print ("Username tidak ditemukan")

#### Tugas Akhir
# Menu Interaktif

# Program Sistem Penilaian Siswa
nama = input("Masukkan nama : ")
nilai = int(input("Masukkan nilai : "))

if nilai >= 90 and nilai <= 100 :
    grade = "A"
elif nilai >= 80 and nilai < 90 :
    grade = "B"
elif nilai >= 70 and nilai < 80 :
    grade = "C"
elif nilai >= 60 and nilai < 70 :
    grade = "D"
else :
    grade= "E"

if nilai >= 70 :
    status = "Lulus"
else : 
    status="Tidak Lulus"

print(f"{nama}, Anda mendapat nilai {grade} di mata pelajaran saya, maka anda dinyatakan {status} ujian saya")

