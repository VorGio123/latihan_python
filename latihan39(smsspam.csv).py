#studi kasus metode klasifikasi - dataset deteksi spam
print("===== STUDI KASUS DATASET DETEKSI SPAM =====")

import pandas as pd

data = pd.read_csv("sms_spam.csv", encoding='latin-1', on_bad_lines='skip')

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(data))
print("Nama kolom:", list(data.columns))

#ambil cuma 2 kolom yang penting: label dan teks pesan
data = data[["v1", "v2"]]
data.columns = ["label", "message"]

print("\nDistribusi label:")
print(data["label"].value_counts())

#ubah label jadi angka (spam=1, ham=0)
data["label"] = data["label"].map({"spam": 1, "ham": 0})

#pisahin fitur (X) dan target (y)
X = data["message"]
y = data["label"]

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#ubah teks jadi angka pakai CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

#latih model klasifikasi
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=10, random_state=42)
model.fit(X_train_vec, y_train)

#buat laporan evaluasi
from sklearn.metrics import classification_report

y_pred = model.predict(X_test_vec)
report = classification_report(y_test, y_pred, target_names=["Ham", "Spam"])

print("\n=== CLASSIFICATION REPORT ===")
print(report)