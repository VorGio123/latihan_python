#studi kasus penyetelan hiperparameter ensemble - dataset penjualan supermarket (versi revisi)
print("===== STUDI KASUS DATASET PENJUALAN SUPERMARKET (REVISI) =====")

import pandas as pd

data = pd.read_csv("supermarket_sales.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))

#ubah kolom teks jadi angka (encoding)
data = pd.get_dummies(data, columns=["Branch", "Customer type", "Gender", "Product line", "Payment"])

#pilih fitur yang relevan
#TIDAK memakai Unit price dan Quantity, karena keduanya secara matematis
#langsung membentuk nilai Total (Total = Unit price x Quantity x 1.05)
fitur_encoded = [col for col in data.columns if col.startswith(("Branch_", "Customer type_", "Gender_", "Product line_", "Payment_"))]
X = data[["Rating"] + fitur_encoded]
y = data["Total"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#definisikan grid parameter
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10]
}

#lakukan grid search
grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("\nBest Parameters:", grid_search.best_params_)
print("Best Score (CV):", grid_search.best_score_)

#latih dan evaluasi model akhir
best_model = grid_search.best_estimator_
test_score = best_model.score(X_test, y_test)

print(f"Skor di data test (R²): {test_score:.4f}")