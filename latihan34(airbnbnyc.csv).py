#studi kasus ensemble boosting - dataset harga airbnb
print("===== STUDI KASUS DATASET HARGA AIRBNB =====")

import pandas as pd

data = pd.read_csv("airbnb_nyc.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))
print("Nama kolom:", list(data.columns))

#buang baris yang harganya 0 (kemungkinan data error/tidak valid)
data = data[data["price"] > 0]

#ubah kolom teks jadi angka (encoding)
data = pd.get_dummies(data, columns=["neighbourhood_group", "room_type"])

#pilih fitur yang relevan
fitur_encoded = [col for col in data.columns if "neighbourhood_group_" in col or "room_type_" in col]
X = data[["minimum_nights", "number_of_reviews", "availability_365"] + fitur_encoded]
y = data["price"]

#isi nilai kosong (jika ada) dengan 0
X = X.fillna(0)

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih model gradient boosting
from sklearn.ensemble import GradientBoostingRegressor

gb = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb.fit(X_train, y_train)

#evaluasi model
from sklearn.metrics import mean_squared_error
import numpy as np

y_pred = gb.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"\nMSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")

#menyetel hyperparameter - coba beberapa learning_rate dan n_estimators
print("\n=== PERCOBAAN BERBAGAI HYPERPARAMETER ===")

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

param_combinations = [
    {"n_estimators": 50, "learning_rate": 0.1},
    {"n_estimators": 100, "learning_rate": 0.1},
    {"n_estimators": 100, "learning_rate": 0.05},
    {"n_estimators": 200, "learning_rate": 0.05},
]

for params in param_combinations:
    gb_test = GradientBoostingRegressor(
        n_estimators=params["n_estimators"],
        learning_rate=params["learning_rate"],
        random_state=42
    )
    gb_test.fit(X_train, y_train)
    y_pred_test = gb_test.predict(X_test)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
    print(f"n_estimators={params['n_estimators']}, learning_rate={params['learning_rate']}, RMSE={rmse_test:.2f}")