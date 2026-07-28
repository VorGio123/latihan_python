#studi kasus pohon keputusan dalam klasifikasi - dataset churn pelanggan
print("===== STUDI KASUS DATASET CHURN PELANGGAN =====")

import pandas as pd

#baca file csv
data = pd.read_csv("telco_churn.csv")

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))

#ubah kolom Churn dari teks (Yes/No) jadi angka (1/0)
data["Churn"] = data["Churn"].map({"Yes": 1, "No": 0})

#ubah kolom Contract (3 kategori teks) jadi beberapa kolom angka 0/1
data = pd.get_dummies(data, columns=["Contract"])

#lihat nama kolom baru hasil get_dummies
print("Nama kolom setelah encoding:", [col for col in data.columns if "Contract" in col])

#pilih fitur sesuai studi kasus: monthly_charges, tenure, contract_type
fitur_kontrak = [col for col in data.columns if "Contract" in col]
X = data[["MonthlyCharges", "tenure"] + fitur_kontrak]
y = data["Churn"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih pohon keputusan
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=5, random_state=42)
tree.fit(X_train, y_train)

#evaluasi metrik
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

y_pred = tree.predict(X_test)
y_proba = tree.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_proba)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"ROC-AUC: {roc_auc:.4f}")