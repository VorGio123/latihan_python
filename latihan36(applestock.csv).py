#studi kasus baseline vs model ML - dataset harga saham
print("===== STUDI KASUS DATASET HARGA SAHAM (BASELINE) =====")

import pandas as pd

data = pd.read_csv("apple_stock.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))
print("Nama kolom:", list(data.columns))

#pilih fitur: pakai harga open, high, low buat nebak close
X = data[["AAPL.Open", "AAPL.High", "AAPL.Low"]]
y = data["AAPL.Close"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#langkah 1: latih model baseline (dummy - cuma nebak rata-rata)
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error

dummy = DummyRegressor(strategy='mean')
dummy.fit(X_train, y_train)
baseline_mse = mean_squared_error(y_test, dummy.predict(X_test))

#langkah 2: latih model ML yang lebih kompleks (linear regression)
from sklearn.linear_model import LinearRegression

model_ml = LinearRegression()
model_ml.fit(X_train, y_train)
ml_mse = mean_squared_error(y_test, model_ml.predict(X_test))

#langkah 3: bandingkan kedua model
print(f"\nBaseline (Dummy) MSE: {baseline_mse:.4f}")
print(f"Model ML (Linear Regression) MSE: {ml_mse:.4f}")

improvement = ((baseline_mse - ml_mse) / baseline_mse) * 100
print(f"Peningkatan: {improvement:.2f}%")