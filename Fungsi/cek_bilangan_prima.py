#Buatlah fungsi untuk menentukan apakah suatu bilangan adalah bilangan prima atau bukan.


def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Contoh penggunaan
bilangan = 29  # Ubah sesuai bilangan yang ingin diuji
if is_prima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")
