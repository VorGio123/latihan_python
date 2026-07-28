#studi kasus pohon keputusan dalam regresi - dataset sewa sepeda
print("===== STUDI KASUS DATASET SEWA SEPEDA (REGRESI) =====")

import pandas as pd

#baca file csv yang udah ada dari modul sebelumnya
data = pd.read_csv("bike_sharing.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))

#pilih fitur sesuai studi kasus: suhu, kelembapan, kondisi cuaca
#(temp = suhu, hum = kelembapan, weathersit = kondisi cuaca)
X = data[["temp", "hum", "weathersit"]]
y = data["cnt"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih pohon keputusan regresi
from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
tree_reg.fit(X_train, y_train)

#evaluasi model
from sklearn.metrics import mean_squared_error, mean_absolute_error

y_pred = tree_reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = tree_reg.score(X_test, y_test)

print(f"\nMSE: {mse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")