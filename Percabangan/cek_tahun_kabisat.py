#Buatlah program untuk menentukan apakah suatu tahun yang 
# diinputkan adalah tahun kabisat atau bukan.

# Input tahun dari pengguna
tahun_a =2014
tahun_b = 2020
# Menentukan apakah tahun kabisat atau bukan
if (tahun_a % 4 == 0 and tahun_a % 100 != 0) or (tahun_a % 400 == 0):
    print(f"{tahun_a} adalah tahun kabisat.")
else:
    print(f"{tahun_a} bukan tahun kabisat.")
# Menentukan apakah tahun kabisat atau bukan
if (tahun_b % 4 == 0 and tahun_b % 100 != 0) or (tahun_b % 400 == 0):
    print(f"{tahun_b} adalah tahun kabisat.")
else:
    print(f"{tahun_b} bukan tahun kabisat.")
