#studi kasus model linier untuk klasifikasi - dataset default kartu kredit
print("===== STUDI KASUS DATASET DEFAULT KARTU KREDIT =====")

import pandas as pd

data = pd.read_csv("credit_default.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))

#pilih fitur sesuai studi kasus: limit kredit, umur, riwayat pembayaran
X = data[["LIMIT_BAL", "AGE", "PAY_0", "BILL_AMT1", "PAY_AMT1"]]
y = data["default.payment.next.month"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih model regresi logistik
from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

#evaluasi model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_pred = log_reg.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")

#interpretasi koefisien
print("\nKoefisien:", log_reg.coef_)