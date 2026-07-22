#membaca dataset
print("===== STUDI KASUS DATASET HARGA RUMAH BOSTON =====")

import pandas as pd

data = pd.read_csv("boston.csv")

print("Dataset berhasil dimuat.")

#melihat dataset
print("\n===== Lima Data Pertama =====")
print(data.head())

#memilihi fitur dan target
print("\n===== Menentukan Fitur dan Target =====")

# Fitur
X = data[["CRIM", "RM", "AGE"]]

# Target
y = data["MEDV"]

print(X.head())

print("\nTarget:")
print(y.head())

#membagi data
print("\n===== Membagi Data Latih dan Data Uji =====")
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Jumlah data latih :", len(X_train))
print("Jumlah data uji   :", len(X_test))

#melatih model
print("\n===== Memilih dan Melatih Model =====")
from sklearn.linear_model import LinearRegression

# Membuat model Linear Regression
model = LinearRegression()

# Melatih model menggunakan data latih
model.fit(X_train, y_train)

print("Model berhasil dilatih.")

#mengevaluasi model
print("\n===== Prediksi dan Evaluasi Model =====")
from sklearn.metrics import mean_squared_error

# Melakukan prediksi menggunakan data uji
y_pred = model.predict(X_test)

# Menghitung Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

print("Hasil Prediksi:")
print(y_pred)

print("\nMean Squared Error (MSE):")
print(mse)

#menginterpretesi hasil
print("\n===== Menginterpretasi Hasil =====")
if mse < 10:
    print("Model memiliki performa yang sangat baik karena nilai MSE kecil.")
elif mse < 100:
    print("Model memiliki performa yang cukup baik.")
else:
    print("Model masih kurang baik karena nilai MSE cukup besar.")