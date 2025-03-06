"""
Buatlah program untuk menentukan grade nilai mahasiswa berdasarkan range:
A (85-100), B (70-84), C (60-69), D (50-59), E (0-49)
"""



# Nilai mahasiswa langsung diinputkan dalam program
nilai = int(input("masukan nilai : "))
# Menentukan grade berdasarkan range nilai
if 85 <= nilai <= 100:
    grade = "A"
elif 70 <= nilai < 85:
    grade = "B"
elif 60 <= nilai < 70:
    grade = "C"
elif 50 <= nilai < 60:
    grade = "D"
elif 0 <= nilai < 50:
    grade = "E"
else:
    grade = "Nilai tidak valid"

# Menampilkan hasil
print(f"Nilai mahasiswa: {nilai}")
print(f"Grade: {grade}")
