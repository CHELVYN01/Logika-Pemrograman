#Buatlah program untuk mencetak deret bilangan Fibonacci sebanyak 20 bilangan.

# Jumlah bilangan Fibonacci yang akan dicetak
jumlah_bilangan = 20

# Inisialisasi dua bilangan pertama dalam deret Fibonacci
fib1, fib2 = 0, 1

# Menampilkan bilangan Fibonacci pertama
print("Deret Fibonacci:")
print(fib1, fib2, end=" ")

# Menggunakan perulangan untuk mencetak bilangan Fibonacci berikutnya
for _ in range(jumlah_bilangan - 2):
    fib_next = fib1 + fib2
    print(fib_next, end=" ")
    fib1, fib2 = fib2, fib_next

print()