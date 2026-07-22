#numpy
import numpy as np

#array numpy 1D
print("===== Membuat Array 1 Dimensi =====")

arr1 = np.array([1, 2, 3, 4])

print(arr1)

#array numpy 2D
print("\n===== Membuat Array 2 Dimensi =====")

arr2 = np.array([
    [1, 2],
    [3, 4]
])

print(arr2)

#shadpe array 2D
print("\n===== Melihat Shape Array =====")

print(arr2.shape)

#size 2D
print("\n===== Melihat Jumlah Data =====")

print(arr2.size)

#dtype 2D
print("\n===== Melihat Tipe Data =====")

print(arr2.dtype)

#array berisi nol
print("\n===== Membuat Array Berisi Nol =====")

zeros_array = np.zeros((3, 4))

print(zeros_array)

#array berisi satu
print("\n===== Membuat Array Berisi Satu =====")

ones_array = np.ones((2, 3))

print(ones_array)

#array random
print("\n===== Membuat Angka Acak =====")

random_array = np.random.rand(2, 3)

print(random_array)

#angka acak 0-100
print("\n===== Nilai Ujian Acak =====")

scores = np.random.rand(5, 3) * 100

print(scores)

#angka berurutan secara otomatis
print("\n===== Membuat Angka Berurutan =====")

range_array = np.arange(10)

print(range_array)

#menentukan jarak
print("\n===== Angka Berurutan Kelipatan 2 =====")

kelipatan = np.arange(0, 10, 2)

print(kelipatan)

#jarak yang sama antara awal dan akhir
print("\n===== Membuat Angka dengan linspace() =====")

linspace_array = np.linspace(0, 10, 6)

print(linspace_array)

#contoh linspace 2
print("\n===== Contoh linspace Kedua =====")

contoh = np.linspace(1, 5, 9)

print(contoh)
