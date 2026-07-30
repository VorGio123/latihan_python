#studi kasus metrik regresi - dataset harga rumah california
print("===== STUDI KASUS DATASET HARGA RUMAH =====")

from sklearn.datasets import fetch_california_housing
import pandas as pd

#load dataset bawaan sklearn
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(X))
print("Nama fitur:", list(X.columns))

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih model regresi
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

#hitung metrik: MAE, RMSE, R²
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\nMAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")