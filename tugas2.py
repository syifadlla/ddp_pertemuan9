#2. Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.

def is_genap(bilangan):
    hitung= bilangan % 2 == 0 #rumus modulus
    return hitung #mengembalikan nilai fahrenheit

angka= 4
hasil= is_genap(angka)
print(f'A.) Bilangan {angka} bernilai {hasil}')

angka2= 7
hasil2= is_genap(angka2)
print(f'B.) Bilangan {angka2} bernilai {hasil2}')