#menentukan bilangan genap atau ganjil#
number = 7

if number % 2 == 0:
    print(f"{number} adalah bilangan genap.")
else:
    print(f"{number} adalah bilangan ganjil.")

#validasi input    
    user_input = input("Masukkan angka positif: ")

if user_input.isdigit():
    number = int(user_input)

    if number > 0:
        print(f"Anda memasukkan angka positif yang valid: {number}")
    else:
        print("Angka harus lebih besar dari nol.")
else:
    print("Input tidak valid. Masukkan angka numerik.")

#sistem penilaian#
score = 78

if score >= 90:
    grade = "A"
    feedback = "Kerja luar biasa!"
elif score >= 80:
    grade = "B"
    feedback = "Bagus sekali!"
elif score >= 70:
    grade = "C"
    feedback = "Tetap tingkatkan."
else:
    grade = "F"
    feedback = "Anda perlu belajar lebih keras."

print(f"Nilai: {grade}")
print(f"Umpan Balik: {feedback}")

#membuat list#
buah = ["apel", "pisang", "ceri"]

print(buah)

#list campuran#
campuran = [1, "apel", True, 3.14]

print(campuran)

#list kosong#
kosong = []

print(kosong)

#mengakses index#
buah = ["apel", "pisang", "ceri"]

print(buah[0])
print(buah[1])
print(buah[-1])

#mengubah elemen list#
buah = ["apel", "pisang", "ceri"]

buah[1] = "blueberry"

print(buah)

#append()#
buah = ["apel", "pisang", "ceri"]

buah.append("dragonfruit")

print(buah)

#insert()#
buah = ["apel", "pisang", "ceri"]

buah.insert(1, "alpukat")

print(buah)

#extend()
buah = ["apel", "pisang", "ceri"]

buah.extend(["anggur", "kiwi"])

print(buah)

#remove()#
buah = ["apel", "pisang", "ceri"]

buah.remove("pisang")

print(buah)

#pop()#
buah = ["apel", "pisang", "ceri"]

buah_dihapus = buah.pop(0)

print(buah_dihapus)
print(buah)

#del#
buah = ["apel", "pisang", "ceri"]

del buah[1]

print(buah)

#clear()#
buah = ["apel", "pisang", "ceri"]

buah.clear()

print(buah)

#len()
buah = ["apel", "pisang", "ceri"]

print(len(buah))

#for#
buah = ["apel", "pisang", "ceri"]

for b in buah:
    print(b)

#enumerate()#
buah = ["apel", "pisang", "ceri"]

for index, isi in enumerate(buah):
    print(index, isi)

#list comprehension#
# buah = ["apel", "pisang", "ceri"]

for index, isi in enumerate(buah):
    print(index, isi)

#daftar belanja#
belanja = ["Beras", "Minyak", "Gula", "Telur"]

print("Daftar Belanja")

for barang in belanja:
    print("-", barang)

#nilai siswa#
nilai = [80, 75, 90, 85]

print("Daftar Nilai")

for n in nilai:
    print(n)

#menghitung jumlah nilai#
nilai = [80, 75, 90, 85]

total = sum(nilai)

print("Jumlah nilai:", total)

#mencari nilai terbesar#
nilai = [80, 75, 90, 85]

print(max(nilai))

#mencari nilai terbesar#
nilai = [80, 75, 90, 85]

print(min(nilai))

#mengurutkan data#
angka = [30, 10, 50, 20]

angka.sort()

print(angka)

#membalikkan urutan listt#
angka = [10, 20, 30, 40]

angka.reverse()

print(angka)