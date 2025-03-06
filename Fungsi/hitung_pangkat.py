#Buatlah fungsi untuk menghitung pangkat dari suatu bilangan (misalnya, a^b).


def hitung_pangkat(a, b):
    return a ** b

basis = int(input("masukan nilai basis :"))
pangkat = int(input("masukan nilai pangkatnya :"))

hasil = hitung_pangkat(basis, pangkat)
print(f"{basis}^{pangkat} = {hasil}")
