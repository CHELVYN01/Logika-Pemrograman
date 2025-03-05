#Buatlah program untuk menghitung jumlah digit dari suatu bilangan yang diinputkan.

# Input bilangan dari pengguna
bilangan = 2000

# Menghitung jumlah digit menggunakan perulangan
jumlah_digit = 0
angka = abs(bilangan)
while angka > 0:
    angka //= 10
    jumlah_digit += 1

# Menampilkan hasil
print(f"Jumlah digit dari bilangan {bilangan} adalah {jumlah_digit}")