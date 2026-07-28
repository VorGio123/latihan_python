#studi kasus hiperparameter pohon keputusan - dataset kebisingan sayap pesawat
print("===== STUDI KASUS DATASET KEBISINGAN SAYAP PESAWAT =====")

import pandas as pd

data = pd.read_csv("airfoil_noise.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))

#pisahin fitur (X) dan target (y)
X = data.drop("SoundLevel", axis=1)
y = data["SoundLevel"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#definisikan grid parameter
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

param_grid = {
    'max_depth': [3, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

#lakukan pencarian grid
grid_search = GridSearchCV(DecisionTreeRegressor(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("\nBest Parameters:", grid_search.best_params_)
print("Best Score (CV):", grid_search.best_score_)

#latih dan evaluasi model akhir pakai parameter terbaik
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test, y_test)

print(f"Skor di data test (R²): {test_score:.4f}")