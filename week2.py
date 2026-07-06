## CEKLIST MINGGU 2 ##

#Program luas bangun datar

#Segitiga
alas = float(input("Masukkan alas segitiga : "))
tinggi = float(input("Masukkan tinggi segitiga : "))
luas_segitiga = (alas * tinggi / 2)
print(f"Luas segitiga dengan alas {alas} cm & tinggi {tinggi} cm adalah {luas_segitiga:.2f} cm^2")

#Persegi Panjang
panjang = float(input("Masukkan panjang persegi panjang : "))
lebar = float(input("Masukkan lebar persegi panjang : "))
luas_persegi_panjang = (panjang * lebar)
print (f"Luas persegi panjang dengan panjang {panjang} cm & lebar {lebar} cm adalah {luas_persegi_panjang} cm^2")

#lingkaran
jari2 = float(input("Masukkan jari - jari lingkaran : "))
luas_lingkaran = (jari2 * 22 / 7)
print(f"Luas lingkaran dengan jari - jari {jari2} cm adalah {luas_lingkaran:.2f} cm^2")

#Persegi
sisi = float(input("Masukkan sisi persegi : "))
luas_persegi = (sisi**2)
print(f"Luas persegi dengan sisi {sisi} cm adalah {luas_persegi} cm^2")


# Program Belanja Bulanan
beras = 13000
minyak_goreng = 16000
sabun_mandi = 4500
total_belanja = int(beras * 3 + minyak_goreng + sabun_mandi * 2 )
print("Ibu membeli 3 kg beras dengan harga Rp13.000 per kg\n1 liter minyak goreng seharga Rp16.000\n2 sabun mandi seharga Rp4.500 per buah.\nBerapa total belanjaan Ibu?")
print(f"\nJawaban : \nTotal belanjaan ibu adalah Rp {total_belanja:,.0f}")


#Program Menghitung Umur
nama = input("Masukkan nama anda : ")
umur = int(input("Masukkan umur anda : "))
print(f"\nHalo, {nama} \nTahun depan kamu berumur {umur + 1} tahun. ")


#Program Perbandingan Dua Angka
a = 28
b = 45

print(f"{a} < {b}, {a < b}")
print(f"{a} > {b}, {a > b}")
print(f"{a} != {b}, {a != b}")
print(f"{a} == {b}, {a == b}")
print(f"{a} <= {b}, {a <= b}")
print(f"{a} >= {b}, {a >= b}")


#Program Kelayakan Ujian
