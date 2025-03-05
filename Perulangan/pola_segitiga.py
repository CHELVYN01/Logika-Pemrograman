"""
Buatlah program untuk mencetak pola segitiga siku-siku menggunakan karakter *.
Contoh:
*
**
***
****
*****
"""

# Menentukan jumlah baris
jumlah_baris = 5  # Ubah sesuai dengan tinggi segitiga yang diinginkan

# Mencetak pola segitiga menggunakan perulangan
for i in range(1, jumlah_baris + 1):
    print('*' * i)
