#Buatlah fungsi untuk menghitung luas lingkaran dengan parameter jari-jari.


#gunakan import math
import math

# Fungsi untuk menghitung luas lingkaran dengan parameter jari-jari
def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2



jari_jari = int(input("Masukan Jari-jarin yang ingin di hitung:"))

luas = hitung_luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
