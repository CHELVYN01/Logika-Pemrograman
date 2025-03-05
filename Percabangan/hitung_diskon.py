"""
Buatlah program untuk menghitung diskon pembelian berdasarkan total belanja:
Jika total belanja > 1.000.000, diskon 10%.
Jika total belanja > 500.000, diskon 5%.
Selain itu, tidak ada diskon.
"""
# Total belanja langsung diinputkan dalam program
total_belanja = 750000  # Ubah sesuai dengan total belanja yang diinginkan

# Menentukan diskon
if total_belanja > 1000000:
    diskon = 0.10 * total_belanja
elif total_belanja > 500000:
    diskon = 0.05 * total_belanja
else:
    diskon = 0.0

# Menghitung total setelah diskon
total_bayar = total_belanja - diskon

# Menampilkan hasil
print(f"Total belanja: Rp{total_belanja:,.2f}")
print(f"Diskon: Rp{diskon:,.2f}")
print(f"Total yang harus dibayar: Rp{total_bayar:,.2f}")
