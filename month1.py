## Tugas Akhir Bulan 1 ##

import random


while True :
    print (f"\n### SELAMAT DATANG DI PROGRAM APLIKASI MINI ###\n\n Pilih salah satu fitur :\n\t1. Kalkulator Sederhana\n\t2. Konverter Suhu\n\t3. Sistem Penilaian Siswa\n\t4. Game Tebak Angka\n\t5. Keluar dari Aplikasi")
    fitur = int(input("Masukkan fitur yang diinginkan : "))
    if fitur == 1 :
        print(f"\nSelamat datang di fitur kalkulator sederhana.\nCara penggunaan :\n\t1. Masukkan angka pertama\n\t2. Masukkan angka kedua\n\t3. Masukkan operasi yang diinginkan (+, -, x, atau /)\n\t4. Hasil operasi akan ditampilkan di layar")
        while True :
            angka1 = float(input("\nMasukkan angka pertama : "))
            angka2 = float(input("Masukkan angka kedua : "))
            operasi = input("Masukkan operasi yang diinginkan : ")
            if operasi == "+" :
                hasil = angka1 + angka2
                print(f"Hasil operasi adalah {hasil}")
            elif operasi == "-" :
                hasil = angka1 - angka2
                print(f"Hasil operasi adalah {hasil}")
            elif operasi == "x" :
                hasil = angka1*angka2
                print(f"Hasil operasi adalah {hasil}")
            elif operasi == "/" :
                hasil = angka1/angka2
                print(f"Hasil operasi adalah {hasil}")
            else :
                print("Operasi tidak valid")

            iflanjut = input("\nApakah anda tetap ingin menggunakan fitur ini? (y/n) : ")
            if iflanjut == "n" :
                break

    if fitur == 2 :
        print(f"\nSelamat datang di fitur konverter suhu.\nCara penggunaan :\n\t1. Masukkan satuan suhu yang diinginkan (C, F, K, atau R)\n\t2. Masukkan suhu yang ingin dikonversi\n\t3. Hasil konversi akan ditampilkan di layar")
        while True :
            satuan= input("\nMasukkan satuan suhu yang diinginkan (C, F, K, atau R) : " )
            suhu = float(input("Masukkan suhu : "))
            if satuan == "C" :
                suhu_r = suhu * 4/5
                suhu_f = suhu *9/5 + 32
                suhu_k = suhu + 273.15
                print(f"\nHasil konversi suhu {suhu} C\n\t- Reamur\t: {suhu_r} R\n\t- Fahrenheit\t: {suhu_f} F\n\t- Kelvin\t: {suhu_k} K")

            elif satuan == "R" :    
                suhu_c = suhu *5/4
                suhu_f = suhu *9/4 + 32
                suhu_k = suhu *5/4 +273.15
                print(f"\nHasil konversi suhu {suhu} R\n\t- Celcius\t: {suhu_c} C\n\t- Fahrenheit\t: {suhu_f} F\n\t- Kelvin\t: {suhu_k} K")
        
            elif satuan == "F" :
                suhu_c = (suhu - 32) *5/9
                suhu_r = (suhu - 32) *4/9
                suhu_k = (suhu - 32) *5/9 + 273.15
                print(f"\nHasil konversi suhu {suhu} F\n\t- Celcius\t: {suhu_c} C\n\t- Reamur\t: {suhu_r} R\n\t- Kelvin\t: {suhu_k} K")

            elif satuan == "K" :
                suhu_c = suhu - 273.15
                suhu_r = (suhu - 273.15) *4/5
                suhu_f = (suhu - 273.15) *9/5 + 32
                print(f"\nHasil konversi suhu {suhu} K\n\t- Celcius\t: {suhu_c} C\n\t- Reamur\t: {suhu_r} R\n\t- Fahrenheit\t: {suhu_f} F")

            iflanjut = input("\nApakah anda tetap ingin menggunakan fitur ini? (y/n) : ")
            if iflanjut == "n" :
                break

    if fitur == 3 :
        print (f"\nSelamat datang di fitur sistem penilaian siswa. \nCara penggunaan :\n\t1. Masukkan nama siswa\n\t2. Masukkan nilai siswa\n\t3. Hasil penilaian akan ditampilkan di layar.")
        while True :
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
            print(f"\n{nama}, Anda mendapat nilai {grade} di mata pelajaran saya, maka anda dinyatakan {status} ujian saya")

            iflanjut = input("\nApakah anda tetap ingin menggunakan fitur ini? (y/n) : ")
            if iflanjut == "n" :
                break

    if fitur == 4 :
        print(f"\nSelamat datang di fitur game tebak angka \nCara penggunaan :\n\t1. Akan ditetapkan angka pilihan secara acak oleh sistem\n\t2. Angka berada pada rentang 1 - 100\n\t3. Anda diminta untuk menebak angka yang telah ditetapkan oleh sistem\n\t4. Anda memiliki kesempatan 10 kali untuk menebak\n\t5. Jika anda menebak angka yang benar, anda menang")
        while True :
            angka = int(input("\nMasukkan angka pilihan anda : "))
            jawaban = random.randint(1,100)
            jumlah_percobaan = 0
            while angka != jawaban :
                jumlah_percobaan += 1
                if jumlah_percobaan == 10 :
                    print (f"Percobaan anda habis, anda kalah\nJawaban yang benar adalah : {jawaban}")
                    break
                elif angka < jawaban : 
                    print ("tebakan anda terlalu kecil, coba lagi")
                elif angka > jawaban :
                    print ("tebakan anda terlalu besar")
                angka = int(input("Masukkan angka pilihan anda : "))

            if angka == jawaban : 
                print (f"Selamat jawaban anda benar dengan jumlah percobaan sebanyak {jumlah_percobaan} kali ")

            iflanjut = input("\nApakah anda tetap ingin menggunakan fitur ini? (y/n) : ")
            if iflanjut == "n" :
                break
    
    if fitur == 5 :
        break

    iflanjut = input("\nApakah anda ingin melanjutkan ke fitur lain? (y/n) : ")

    if iflanjut == "n" :
        break

print(f"\nAplikasi Selesai")



