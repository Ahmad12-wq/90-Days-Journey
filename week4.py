#### Week 4 ####

## Hari 22 ##
# Perulangan for

for i in range (10,0,-1) :
    print (i, end=" ")

for n in range (10) :
    print ("Ahmad adel")

for a in range (0,101,5) :
    print (a)

for b in range (1,21) :
    print (f"Hari ke -{b} belajar python")

## Hari 23 ##
# Range ()

# Bilangan genap dari 2 sampai 100
print("Bilangan genap dari 2 sampai 100 : \n")
for i in range (2,101,2) :
    print (i, end=" ")

print ("\n")

# Bilangan ganjil dari 1 sampai 99
print("Bilangan ganjil dari 1 sampai 99 :\n")

for i in range (1,100,2) :
    print (i, end=" ")

# Kelipatan 7
print("\n Kelipatan 7 dari 1 sampai 100 : \n")
for i in range (7,100,7) :
    print(i, end= " ")

# Hitung mundur 20 ke 1
print("\n Hitung mundur dari 20 ke 1 : \n")
for i in range (20,0,-1):
    print (i, end = " ")

# Hitung mundur 100 ke 0 kelipatan 5
print("\n Hitung mundur dari 100 ke 0 dengan kelipatan 5 : \n")
for i in range (100,0,-5) :
    print (i, end=" ")

## Hari 24 ##
# Perulangan while

# Hitung 1 sampai 10 
print("\n Hitung 1 sampai 10 : \n")
angka = 1
while angka <= 10 :
    print (angka, end = " " )
    angka +=1

# Hitung mundur 10 sampai 1 
print ("\n Hitung mundur 10 sampai 1 : \n")
angka = 10
while angka >=1 :
    print (angka, end = " ")
    angka -=1

#Kelipatan 3
print("\n Kelipatan 3 dari 1 sampai 100 : \n")
angka = 3 
while angka <= 100 :
    print (angka, end = " ")
    angka += 3 

# Program masukkan angka
angka = int(input("\n Masukkan angka : "))
while angka != 0 :
    print (angka)
    angka = int(input("Masukkan angka : "))

## Hari 25 ##
# Break & Continue

# Cetak angka 1 - 100 berhenti di 50
print("\n Cetak angka 1 - 100, berhenti di 50 : \n")
for i in range (1, 101) :
    if i >= 51 :
        break
    print (i, end = " ")

# Cetak 1 - 20 lewati angka 7
print("\nCetak angka 1 - 20, lewati angka 7 : \n")
for i in range (1,21) :
    if i == 7:
        continue
    print(i, end = " ")

# Cetak angka 1 - 100 lewati 10, 20, 30, 40, 50
print("\nCetak angka 1 - 100, lewati 10, 20, 30, 40, 50 : \n")
for i in range (1,101) :
    if i % 10 == 0 and i <= 50:
        continue
    print (i, end = " ")

## Hari 26 ##
# Nested Loop
 
# Membuat pola segitiga bintang
print ("\nMembuat pola segitiga bintang : \n")
for i in range (5) :
    for j in range ( 1, i +1) :
        print ("*", end = " ")
    print ()

for i in range (5) :
    for j in range (5) :
        print ("*", end = " ")
    print ()

for i in range (4) :
    for j in range (8) :
        print("#", end = " " )
    print ()

n = int(input("Masukkan jumlah baris : "))
angka = 1
jumlah = 0
while angka <= n :
    jumlah += angka
    angka += 1
print (f"\n jumlah angka 1 - {n} adalah {jumlah}")

i = 5
faktorial = 1
while i > 0 :
    faktorial *= i
    i -= 1
print (f"\n faktorial dari 5 adalah {faktorial}")

# Perkalian 7
for i in range (7, 71, 7) :
    print (f"7 x {i/7} = {i}")

angka = int(input("Masukkan angka yang anda pilih : "))
jawaban = 42
jumlah_percobaan = 0

while angka != jawaban :
    jumlah_percobaan += 1
    if jumlah_percobaan == 5 :
        print ("maaf percobaan anda habis")
        break
    elif angka < jawaban : 
        print ("terlalu kecil")
    elif angka > jawaban :
        print ("terlalu besar")
    angka = int(input("Masukkan angka yang anda pilih : "))

    
while angka == jawaban :
    print (f"selamat jawaban anda benar dengan jumlah percobaan sebanyak {jumlah_percobaan} kali ")
    break





