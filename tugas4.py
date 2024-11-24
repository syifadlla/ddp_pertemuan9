#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens

#bilangan(20) # 1,3,5,7,9,11,13,15,17,19

def perulangan(angka):
    for i in range(1, angka, 2):
        print(i, end=",  ")

perulangan(20)