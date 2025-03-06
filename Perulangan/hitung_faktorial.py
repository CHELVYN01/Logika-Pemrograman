#Buatlah program untuk menghitung faktorial dari suatu bilangan yang diinputkan

bilangan = int(input("input bilangan : "))

# Inisialisasi hasil faktorial
faktorial = 1

# Menghitung faktorial menggunakan perulangan
for i in range(1, bilangan + 1):
    faktorial *= i

# Menampilkan hasil
print(f"Faktorial dari {bilangan} adalah {faktorial}")