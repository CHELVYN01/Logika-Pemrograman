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

jumlah_baris=4

cetak_segitiga_terbalik(jumlah_baris)
