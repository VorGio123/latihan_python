#studi kasus penyempurnaan manual hyperparameter - dataset sewa sepeda
print("===== STUDI KASUS DATASET SEWA SEPEDA =====")

import pandas as pd

#baca file csv
data = pd.read_csv("bike_sharing.csv")

#menampilkan 5 data pertama
print("Dataset berhasil dimuat.")
print(data.head())
print("Jumlah baris:", len(data))

#pisahin fitur (X) dan target (y)
#buang kolom yang gak dipake: instant, dteday, casual, registered
#(casual + registered itu udah nyusun cnt, jadi gak boleh dipake sebagai fitur)
X = data.drop(["instant", "dteday", "casual", "registered", "cnt"], axis=1)
y = data["cnt"]

#import model dan tools evaluasi
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score

#coba beberapa nilai max_depth secara manual
for depth in [3, 5, 10]:
    model = DecisionTreeRegressor(max_depth=depth, random_state=42)
    scores = cross_val_score(model, X, y, cv=5)
    print(f"Depth={depth}, Mean CV Score={scores.mean()}")

#simpan hasil biar bisa dibandingkan
depth_list = [3, 5, 10]
score_list = []

for depth in depth_list:
    model = DecisionTreeRegressor(max_depth=depth, random_state=42)
    scores = cross_val_score(model, X, y, cv=5)
    score_list.append(scores.mean())
    print(f"Depth={depth}, Mean CV Score={scores.mean()}")

#pilih depth dengan skor terbaik
best_index = score_list.index(max(score_list))
best_depth = depth_list[best_index]

print(f"\nDepth optimal: {best_depth}")
print(f"Skor terbaik: {max(score_list)}")