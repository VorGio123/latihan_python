def sapa():
    print("Halo, Nandika!")
    print("Semangat Buat Belajar")

sapa()

def tambah(a, b):
    return a + b

hasil = tambah(5, 7)

print(hasil)

def perkenalan(nama, umur):
    print("Nama saya", nama)
    print("Umur saya", umur)

perkenalan("Nandika", 17)
perkenalan("Candra", 17)

def kali(a, b):
    return a * b

hasil = kali(4, 3)

print(hasil)

def luas_persegi(panjang, lebar):
    return panjang * lebar

luas = luas_persegi(5, 8)

print("Luas =", luas)

def sapa(nama="Candra"):
    print("Halo", nama)

sapa("Nandika")
sapa()

kuadrat = lambda x: x ** 2

print(kuadrat(4))

tambah = lambda a, b: a + b

print(tambah(10, 20))

besar = lambda a, b: a if a > b else b

print(besar(15, 20))

def is_even(number):
    return number % 3 == 0

print(is_even(6))
print(is_even(7))

help(sum)