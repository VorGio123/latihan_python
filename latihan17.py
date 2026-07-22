#studi kasus
print("===== Studi Kasus Prediksi Harga Rumah di California =====")

import pandas as pd

#membaca dataset
data = pd.read_csv("housing.csv")

print("\nDataset berhasil dimuat!")

#menampilkan 5 baris data pertama
print("\n===== 5 DATA PERTAMA =====")
print(data.head())

#info
print("\n===== INFORMASI DATASET =====")
data.info()

#statistik
print("\n===== STATISTIK DATASET =====")
print(data.describe())

print("\n===== Langkah 2.3 : Memeriksa Nilai yang Hilang =====")

# Mengecek jumlah data yang kosong pada setiap kolom
print(data.isnull().sum())

#visual data 
print("\n===== Visualisasi Hubungan Data =====")

import seaborn as sns
import matplotlib.pyplot as plt

#heatmap
print("\n===== Heatmap Korelasi =====")

plt.figure(figsize=(8, 6))

sns.heatmap(
    data.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.show()