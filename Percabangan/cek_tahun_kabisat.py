#Buatlah program untuk menentukan apakah suatu tahun yang 
# diinputkan adalah tahun kabisat atau bukan.

# Input tahun dari pengguna
tahun = int(input("input tahun yang ingin dicek : "))

# Menentukan apakah tahun kabisat atau bukan
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
