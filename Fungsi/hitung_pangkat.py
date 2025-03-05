#Buatlah fungsi untuk menghitung pangkat dari suatu bilangan (misalnya, a^b).


def hitung_pangkat(a, b):
    return a ** b

# Contoh penggunaan
basis = 2  # Ubah sesuai basis yang diinginkan
pangkat = 3  # Ubah sesuai pangkat yang diinginkan
hasil = hitung_pangkat(basis, pangkat)
print(f"{basis}^{pangkat} = {hasil}")
