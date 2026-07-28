#studi kasus regularisasi model linier - dataset kekuatan beton
print("===== STUDI KASUS DATASET KEKUATAN BETON =====")

import pandas as pd

data = pd.read_csv("concrete.csv")

print("Dataset berhasil dimuat.")
print(data.head())
print("Jumlah baris:", len(data))

#pisahin fitur (X) dan target (y)
X = data.drop("strength", axis=1)
y = data["strength"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih model tanpa regularisasi (Linear Regression biasa)
from sklearn.linear_model import LinearRegression, Ridge

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

#latih model dengan regularisasi (Ridge)
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)

#bandingkan kinerja kedua model
linear_score = linear_model.score(X_test, y_test)
ridge_score = ridge_model.score(X_test, y_test)

print(f"\nLinear Regression R²: {linear_score:.4f}")
print(f"Ridge Regression R²: {ridge_score:.4f}")

#bandingkan koefisiennya
print("\nKoefisien Linear Regression:", linear_model.coef_)
print("Koefisien Ridge Regression:", ridge_model.coef_)

#sesuaikan alpha - coba beberapa kekuatan regularisasi berbeda
print("\n=== PERCOBAAN BERBAGAI NILAI ALPHA ===")

alpha_list = [0.1, 1.0, 10.0, 100.0]

for alpha in alpha_list:
    ridge_test = Ridge(alpha=alpha)
    ridge_test.fit(X_train, y_train)
    score = ridge_test.score(X_test, y_test)
    print(f"Alpha={alpha}, R²={score:.4f}")