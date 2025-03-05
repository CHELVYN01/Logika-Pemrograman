"""
Buatlah fungsi untuk mencetak pola segitiga terbalik menggunakan karakter *.
Contoh:
*****
****
***
**
*
"""

def cetak_segitiga_terbalik(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Contoh penggunaan
jumlah_baris = 5  # Ubah sesuai jumlah baris yang diinginkan
cetak_segitiga_terbalik(jumlah_baris)
