#studi kasus stratified cross-validation - dataset penyakit jantung
print("===== STUDI KASUS DATASET PENYAKIT JANTUNG =====")

import pandas as pd

data = pd.read_csv("heart.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))
print("Distribusi target:")
print(data["target"].value_counts())

#pisahin fitur (X) dan target (y)
X = data.drop("target", axis=1)
y = data["target"]

#tentukan stratified k-fold
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier

cv = StratifiedKFold(n_splits=5)
model = DecisionTreeClassifier(max_depth=5, random_state=42)

#evaluasi model pakai stratified cross-validation
scores = cross_val_score(model, X, y, cv=cv)

print(f"\nSkor tiap fold: {scores}")
print(f"Rata-rata skor: {scores.mean():.4f}")
print(f"Standar deviasi: {scores.std():.4f}")