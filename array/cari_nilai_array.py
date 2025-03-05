#Buatlah program untuk mencari suatu bilangan 
#dalam array dan menampilkan indeksnya (jika ditemukan).



# Contoh array bilangan bulat
array_bilangan = [10, 3, 25, 7, 18, 5]

# Bilangan yang ingin dicari (langsung diisi di program)
cari_bilangan = 7  # Ubah sesuai bilangan yang ingin dicari

# Mencari indeks bilangan
if cari_bilangan in array_bilangan:
    indeks = array_bilangan.index(cari_bilangan)
    print(f"Bilangan {cari_bilangan} ditemukan pada indeks {indeks}.")
else:
    print(f"Bilangan {cari_bilangan} tidak ditemukan dalam array.")