#Buatlah fungsi untuk menghitung jumlah bilangan ganjil dalam sebuah array.


def hitung_jumlah_ganjil(array):
    jumlah_ganjil = sum(1 for angka in array if angka % 2 != 0)
    return jumlah_ganjil


array_bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Ubah sesuai dengan array yang diinginkan
hasil = hitung_jumlah_ganjil(array_bilangan)
print(f"Jumlah bilangan ganjil dalam array: {hasil}")