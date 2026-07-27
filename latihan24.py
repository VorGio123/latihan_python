#studi kasus penyempurnaan otomatis hyperparameter - dataset kanker payudara
print("===== STUDI KASUS DATASET KANKER PAYUDARA WISCONSIN =====")

from sklearn.datasets import load_breast_cancer

#load dataset bawaan sklearn
data = load_breast_cancer()
X = data.data
y = data.target

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(X))
print("Nama fitur:", data.feature_names)

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#tentukan grid parameter yang mau dicoba
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

param_grid = {
    'max_depth': [3, 5, 10],
    'min_samples_split': [2, 5, 10]
}

#lakukan pencarian grid (otomatis coba semua kombinasi)
grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("\nBest Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

#latih ulang model pakai parameter terbaik, uji ke data test
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test, y_test)

print(f"\n=== EVALUASI MODEL AKHIR ===")
print(f"Parameter terbaik: {grid_search.best_params_}")
print(f"Skor di data test: {test_score:.4f}")