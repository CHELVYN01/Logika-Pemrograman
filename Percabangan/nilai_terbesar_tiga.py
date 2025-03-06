#Buatlah program untuk menentukan nilai terbesar dari tiga bilangan yang diinputkan.

# Input tiga bilangan secara langsung
bilangan1 = int(input("masukan bilang 1 : "))
bilangan2 = int(input("masukan bilang 2 : "))
bilangan3 = int(input("masukan bilang 3 : "))
# Menentukan bilangan terbesar
nilai_terbesar = max(bilangan1, bilangan2, bilangan3)

# Menampilkan hasil
print(f"Bilangan pertama: {bilangan1}")
print(f"Bilangan kedua: {bilangan2}")
print(f"Bilangan ketiga: {bilangan3}")
print(f"Nilai terbesar adalah: {nilai_terbesar}")
