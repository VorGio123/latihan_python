#studi kasus intuisi model berbasis pohon - dataset spesies iris
print("===== STUDI KASUS DATASET SPESIES IRIS =====")

from sklearn.datasets import load_iris
import pandas as pd

#load dataset bawaan sklearn
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print("Dataset berhasil dimuat.")
print("Jumlah baris:", len(X))
print("Nama fitur:", list(X.columns))
print("Nama spesies:", iris.target_names)

#bagi data jadi data latih dan data uji
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#latih pohon keputusan
from sklearn.tree import DecisionTreeClassifier, export_text

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)

#tampilkan aturan pohon dalam bentuk teks
rules = export_text(tree, feature_names=list(X.columns))
print("\n=== ATURAN POHON KEPUTUSAN ===")
print(rules)

#evaluasi kinerja
accuracy = tree.score(X_test, y_test)
print(f"\nAccuracy: {accuracy:.4f}")

#confusion matrix - matriks kebingungan
from sklearn.metrics import confusion_matrix

y_pred = tree.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

print("\n=== CONFUSION MATRIX ===")
print(cm)