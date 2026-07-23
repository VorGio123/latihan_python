#studi kasus kurva validasi dan kurva pembelajaran - dataset kualitas anggur
print("===== STUDI KASUS DATASET KUALITAS ANGGUR =====")

import pandas as pd

#baca file csv, pemisahnya titik koma (;) bukan koma
data = pd.read_csv("winequality.csv", sep=";")

#bersihin nama kolom dari tanda kutip dan spasi berlebih (jaga-jaga hasil copy-paste)
data.columns = data.columns.str.replace('"', '').str.strip()

#menampilkan 5 data pertama
print("Dataset berhasil dimuat.")
print(data.head())
print("Nama kolom:", list(data.columns))
print("Jumlah baris:", len(data))

#pisahin fitur (X) dan target (y)
#X = semua kolom kecuali quality
#y = kolom quality (nilai kualitas anggur, angka 0-10)
X = data.drop("quality", axis=1)
y = data["quality"]

#import tools buat kurva pembelajaran
from sklearn.model_selection import learning_curve
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#generate kurva pembelajaran
#ini nyoba model dengan ukuran data latihan yang beda-beda (makin banyak makin besar)
train_sizes, train_scores, test_scores = learning_curve(
    LinearRegression(),
    X,
    y,
    cv=5,
    scoring='neg_mean_squared_error'
)

#ubah skor jadi positif (biar gampang dibaca, karena aslinya negatif)
train_mean = -train_scores.mean(axis=1)
test_mean = -test_scores.mean(axis=1)

#gambar grafik kurva pembelajaran
plt.plot(train_sizes, train_mean, label='Training Error')
plt.plot(train_sizes, test_mean, label='Validation Error')
plt.xlabel("Jumlah Data Latihan")
plt.ylabel("Error (MSE)")
plt.title("Kurva Pembelajaran - Kualitas Anggur")
plt.legend()
plt.show()

#interpretasi hasil
selisih_akhir = test_mean[-1] - train_mean[-1]

print(f"\n=== KESIMPULAN ===")
print(f"Training Error di akhir: {train_mean[-1]:.4f}")
print(f"Validation Error di akhir: {test_mean[-1]:.4f}")
print(f"Selisihnya: {selisih_akhir:.4f}")

if selisih_akhir < 0.05:
    print("Dua garis error-nya udah deket-deketan dan sama-sama gak naik-turun lagi di akhir grafik.")
    print("Jadi kalau data ditambah lebih banyak lagi, kemungkinan gak bakal ngaruh banyak,")
    print("soalnya modelnya udah mentok, gak bisa lebih pinter lagi buat data kayak gini.")
else:
    print("Masih ada jarak lumayan jauh antara training sama validation error.")
    print("Jadi kalau datanya ditambah lagi, kemungkinan errornya masih bisa turun.")
    