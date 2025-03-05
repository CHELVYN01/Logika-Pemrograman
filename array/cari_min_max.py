#Buatlah program untuk mencari nilai maksimum dan 
# minimum dari sebuah array bilangan bulat.


# Contoh array bilangan bulat
array_bilangan = [1, 3, 5, 7, 180, 5]

# Inisialisasi nilai minimum dan maksimum
nilai_min = array_bilangan[0]
nilai_max = array_bilangan[0]

# Mencari nilai minimum dan maksimum
total_elemen = len(array_bilangan)
for i in range(total_elemen):
    if array_bilangan[i] < nilai_min:
        nilai_min = array_bilangan[i]
    if array_bilangan[i] > nilai_max:
        nilai_max = array_bilangan[i]

# Menampilkan hasil
print(f"Nilai minimum: {nilai_min}")
print(f"Nilai maksimum: {nilai_max}")
