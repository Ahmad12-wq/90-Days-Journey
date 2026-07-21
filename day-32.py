## Day 32 ##
# Fungsi Bawaan List

nilai = [78, 90, 67, 88, 95]

# Jumlah Nilai
jumlah = sum(nilai)
print(f"Jumlah nilai adalah {jumlah}")

# Nilai Terbesar
nilai_terbesar = max(nilai)
print(f"\nNilai terbesar di kelas adalah {nilai_terbesar}")

# Nilai Terkecil
nilai_terkecil = min(nilai)
print(f"\nNilai terkecil di kelas adalah {nilai_terkecil}")

# Nilai Rata - Rata
panjang = len(nilai)
rata_rata = jumlah/panjang
print(f"\nRata - rata nilai di kelas adalah {rata_rata}")

# Urutan Naik
urut_naik = sorted(nilai)
print(f"\nJika diurutkan dari yang terkecil, maka dapat diurutkan menjadi\n{urut_naik}")

# Urutan turun
urut_turun = sorted(nilai, reverse=True)
print(f"\nJika diurutkan dari yang terbesar, maka dapat diurutkan menjadi\n{urut_turun}")








