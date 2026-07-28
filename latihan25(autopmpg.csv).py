#studi kasus intuisi model linier - dataset auto mpg
print("===== STUDI KASUS DATASET AUTO MPG =====")

import pandas as pd

#baca file csv
data = pd.read_csv("auto_mpg.csv")

#menampilkan 5 data pertama
print("Dataset berhasil dimuat.")
print(data.head())
print("Jumlah baris:", len(data))

#cek apakah ada data kosong/tanda tanya di kolom horsepower
print("Nilai unik horsepower yang aneh:", data[data["horsepower"] == "?"])

#bersihin data: ganti "?" jadi kosong beneran, lalu buang baris yang kosong
data["horsepower"] = pd.to_numeric(data["horsepower"], errors="coerce")
data = data.dropna()

print("Jumlah baris setelah dibersihkan:", len(data))

#pisahin fitur (X) dan target (y)
#pakai displacement dan horsepower sesuai tujuan studi kasus
X = data[["displacement", "horsepower"]]
y = data["mpg"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih model regresi linier
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

#lihat koefisien dan intercept
print("\nCoefficients:", model.coef_)
print("Intercept:", model.intercept_)

#evaluasi model - ngukur seberapa akurat prediksinya
from sklearn.metrics import mean_squared_error

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

print(f"\nMSE: {mse:.4f}")
print(f"R²: {r2:.4f}")