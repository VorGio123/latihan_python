#studi kasus regresi linear - dataset biaya asuransi
print("===== STUDI KASUS DATASET INSURANCE CHARGES =====")

import pandas as pd

#baca file csv
data = pd.read_csv("insurance.csv")

print("Dataset berhasil dimuat.")
print(data.head())
print("Jumlah baris:", len(data))

#ubah kolom smoker dari teks (yes/no) jadi angka (1/0)
#soalnya model gak bisa ngolah teks langsung
data["smoker"] = data["smoker"].map({"yes": 1, "no": 0})

#pilih fitur sesuai studi kasus: age, bmi, smoker
X = data[["age", "bmi", "smoker"]]
y = data["charges"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih model regresi linier
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

#evaluasi model
from sklearn.metrics import mean_squared_error, mean_absolute_error

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

print(f"\nMSE: {mse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"R²: {r2:.4f}")

#visualisasi hasil - bandingin prediksi vs nilai asli
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Biaya Asli (Actual Charges)")
plt.ylabel("Biaya Prediksi (Predicted Charges)")
plt.title("Prediksi vs Aktual - Biaya Asuransi")
plt.show()