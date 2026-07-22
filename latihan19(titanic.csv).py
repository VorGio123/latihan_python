#membaca dataset
print("===== STUDI KASUS DATASET TITANIC =====")

import pandas as pd

data = pd.read_csv("titanic.csv")

print("Dataset berhasil dimuat.")

#menampilkan 5 data pertama
print(data.head())

#fitur kategorikal
print("\n===== Mengidentifikasi Fitur Kategorikal =====")

# Menentukan kolom kategorikal
categorical_cols = ["Pclass", "Embarked"]

print("Kolom kategorikal:")
print(categorical_cols)

#data kategorikal
print("\n===== Mengodekan Data Kategorikal =====")

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ("jarvis", OneHotEncoder(), categorical_cols)
    ]
)

print("Preprocessor berhasil dibuat.")

#membangun pipeline
print("\n===== Membangun Pipeline =====")

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)

print("Pipeline berhasil dibuat.")

#fitur x dan y
print("\n===== Menentukan Fitur dan Target =====")

# Menentukan fitur (X)
X = data[categorical_cols]

# Menentukan target (y)
y = data["Survived"]

print(X.head())

print("\nTarget:")
print(y.head())

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

print("\n===== Melatih dan Mengevaluasi Model =====")

pipeline.fit(X_train, y_train)

score = pipeline.score(X_test, y_test)

print(f"R-squared : {score}")

print("\n===== Menginterpretasi Hasil =====")
if score >= 0.8:
    print("Model memiliki performa yang sangat baik.")
elif score >= 0.5:
    print("Model memiliki performa yang cukup baik.")
else:
    print("Model masih kurang baik dan perlu ditingkatkan.")