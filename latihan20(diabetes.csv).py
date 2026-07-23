#studi kasus dataset diabetes
print("===== STUDI KASUS DATASET DIABETES =====")

import pandas as pd

#baca file csv
data = pd.read_csv("diabetes.csv")

#menampilkan 5 data pertama
print("Dataset berhasil dimuat.")
print(data.head())

#cek jumlah baris datanya
print("Jumlah baris:", len(data))

#import model decision tree buat klasifikasi (karena target isinya 0/1)
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

#pisahin fitur (X) dan target (y)
#X = semua kolom kecuali target, ini yang dipakai buat "nebak"
#y = kolom target, ini jawaban yang mau ditebak
X = data.drop("target", axis=1)
y = data["target"]

#bagi data jadi data latihan (80%) dan data ujian (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#tempat nyimpen nilai akurasi tiap kedalaman pohon
train_scores = []
test_scores = []

#coba latih model dengan kedalaman pohon dari 1 sampai 9
for depth in range(1, 10):
    #bikin model dengan kedalaman tertentu
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    
    #latih model pakai data training
    model.fit(X_train, y_train)
    
    #cek nilai akurasi di data training (soal yang udah pernah dilihat)
    train_scores.append(model.score(X_train, y_train))
    
    #cek nilai akurasi di data testing (soal baru yang belum pernah dilihat)
    test_scores.append(model.score(X_test, y_test))

#gambar grafik buat lihat pola overfitting/underfitting
import matplotlib.pyplot as plt

plt.plot(range(1, 10), train_scores, label="Training Score")
plt.plot(range(1, 10), test_scores, label="Testing Score")
plt.xlabel("Kedalaman Pohon (max_depth)")
plt.ylabel("Akurasi")
plt.title("Overfitting vs Underfitting")
plt.legend()
plt.show()

#cari depth dengan testing score tertinggi
best_depth = test_scores.index(max(test_scores)) + 1
print(f"Kedalaman optimal (max_depth): {best_depth}")
print(f"Testing Score tertinggi: {max(test_scores):.4f}")

#interpretasi hasil
best_depth = test_scores.index(max(test_scores)) + 1
selisih_akhir = train_scores[-1] - test_scores[-1]

print(f"\n=== KESIMPULAN ===")
print(f"Kedalaman optimal (max_depth): {best_depth}")
print(f"Testing Score tertinggi: {max(test_scores):.4f}")
print(f"Training Score di depth terakhir: {train_scores[-1]:.4f}")
print(f"Testing Score di depth terakhir: {test_scores[-1]:.4f}")
print(f"Selisihnya: {selisih_akhir:.4f}")

if selisih_akhir > 0.1:
    print("Di depth yang paling tinggi (9), training score-nya jauh lebih gede dari testing score.")
    print("Jadi modelnya kena overfitting, kebanyakan hafalin data latihan doang.")
    print(f"Makanya depth yang lebih cocok dipake itu depth {best_depth}, soalnya di situ testing score-nya paling gede.")
else:
    print("Selisih training sama testing score gak terlalu jauh, jadi modelnya masih aman, gak overfitting parah.")
    ##