#studi kasus nested cross-validation - dataset pinjaman default (HMEQ)
print("===== STUDI KASUS DATASET PINJAMAN DEFAULT (HMEQ) =====")

import pandas as pd

data = pd.read_csv("hmeq.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))
print("Jumlah data kosong per kolom:")
print(data.isnull().sum())

#bersihin data kosong - isi kolom angka dengan median, buang baris yang masih kosong di kolom teks
kolom_angka = data.select_dtypes(include=['float64', 'int64']).columns
data[kolom_angka] = data[kolom_angka].fillna(data[kolom_angka].median())
data = data.dropna()

#ubah kolom teks jadi angka
data = pd.get_dummies(data, columns=["REASON", "JOB"])

print("\nJumlah baris setelah dibersihkan:", len(data))

#pisahin fitur (X) dan target (y)
X = data.drop("BAD", axis=1)
y = data["BAD"]

#tentukan inner dan outer loop
from sklearn.model_selection import KFold, GridSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier

#inner loop: buat nyari hyperparameter terbaik (dibungkus dalam GridSearchCV)
param_grid = {'max_depth': [3, 5, 10]}
inner_cv = KFold(n_splits=3)
grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=inner_cv)

#outer loop: buat ngukur performa model secara jujur/tidak bias
outer_cv = KFold(n_splits=5)
nested_scores = cross_val_score(grid_search, X, y, cv=outer_cv)

print(f"\nSkor tiap outer fold: {nested_scores}")
print(f"Rata-rata skor (Nested CV): {nested_scores.mean():.4f}")
print(f"Standar deviasi: {nested_scores.std():.4f}")