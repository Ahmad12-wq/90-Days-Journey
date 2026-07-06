## WEEK 5 : LIST ##

# DAY 29 #
# Mengenal List #

buah = [
"Apel",
"Nanas",
"Mangga",
"Pir",
"Sirsak"
]

print(buah)
print(buah[0])
print(buah[1])

mahasiswa = [
    "Ahmad",
    "Bayu",
    "Adit",
    "Asep",
    "Lanco",
    "Tegar"
]

#Cetak Seluruh List
print(mahasiswa)

#Cetak Nama Pertama
print(mahasiswa[0])

#Cetak Nama Terakhir 
print(mahasiswa[-1])

#Cetak Jumlah Data
print(len(mahasiswa))


## Mini Project
# Membuat daftar film
daftar_film = [
    "lord of the ring",
    "haikyuu",
    "hajime no ippo",
    "kingdom",
    "fury",
    "band of brotherhood",
    "the hobbit",
    "fight club",
    "kimi no nawa",
    "rango"
]
print("\nFilm Favorit Ahmad Adel")
for i in range (1,11) :
    print(i,daftar_film[i-1], end=" ")
    print()

## Tantangan
daftar_nilai=[
    85,
    65,
    48,
    89,
    72,
    28,
    98,
    100,
    45
]

#Nilai tertinggi
print(max(daftar_nilai))

#Nilai terendah
print(min(daftar_nilai))

#Rata rata nilai
rata_rata = sum(daftar_nilai)/len(daftar_nilai)
print(rata_rata)



