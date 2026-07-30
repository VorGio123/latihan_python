#studi kasus ensemble bootstrapping - dataset tipe penutup hutan
print("===== STUDI KASUS DATASET TIPE PENUTUP HUTAN =====")

from sklearn.datasets import fetch_covtype
import pandas as pd

#ambil dataset bawaan sklearn (proses download otomatis, bisa agak lama di awal)
print("Sedang memuat dataset, mohon tunggu...")
covtype = fetch_covtype()

X = covtype.data
y = covtype.target

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(X))
print("Jumlah fitur:", X.shape[1])

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih random forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

#evaluasi kinerja
from sklearn.metrics import accuracy_score, f1_score

y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"\nAccuracy: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")

#analisis feature importance
print("\n=== 5 FITUR PALING PENTING ===")
importances = rf.feature_importances_
top_5_idx = importances.argsort()[-5:][::-1]
for idx in top_5_idx:
    print(f"Fitur ke-{idx}: {importances[idx]:.4f}")