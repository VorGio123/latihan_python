#studi kasus trade-off bias vs variance - dataset pengeluaran iklan
print("===== STUDI KASUS DATASET PENGELUARAN IKLAN =====")

import pandas as pd

#baca file csv
data = pd.read_csv("advertising.csv")

#menampilkan 5 data pertama
print("Dataset berhasil dimuat.")
print(data.head())

#pisahin fitur (X) dan target (y)
#X = pengeluaran iklan di TV, Radio, Newspaper
#y = Sales (jumlah penjualan yang mau diprediksi)
X = data.drop("Sales", axis=1)
y = data["Sales"]

#import 2 model yang mau dibandingkan
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import cross_val_score

#uji Linear Regression pakai validasi silang (cross validation)
linear_scores = cross_val_score(
    LinearRegression(), X, y, cv=5, scoring='neg_mean_squared_error'
)

#uji Ridge Regression (versi yang dikasih "rem" biar gak terlalu sensitif)
ridge_scores = cross_val_score(
    Ridge(alpha=1.0), X, y, cv=5, scoring='neg_mean_squared_error'
)

#print hasil (dibalik jadi positif biar gampang dibaca)
print("Linear Regression MSE:", -linear_scores.mean())
print("Ridge Regression MSE:", -ridge_scores.mean())

#latih ulang model (bukan cross validation) biar bisa liat koefisiennya
linear_model = LinearRegression()
linear_model.fit(X, y)

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X, y)

print("\n=== KOEFISIEN MODEL ===")
print("Koefisien Linear Regression:", linear_model.coef_)
print("Koefisien Ridge Regression:", ridge_model.coef_)

#interpretasi hasil
selisih_mse = abs(-linear_scores.mean() - (-ridge_scores.mean()))

print(f"\n=== KESIMPULAN ===")
print(f"Linear Regression MSE: {-linear_scores.mean():.4f}")
print(f"Ridge Regression MSE: {-ridge_scores.mean():.4f}")
print(f"Selisih MSE: {selisih_mse:.6f}")

if selisih_mse < 0.01:
    print("Selisih MSE dua model ini nyaris nggak ada, jadi regularisasi (Ridge)")
    print("gak ngasih perbaikan yang berarti buat dataset ini.")
    print("Kemungkinan datanya emang udah simpel/gak terlalu bervariasi,")
    print("jadi model biasa (Linear Regression) aja udah cukup pas.")
else:
    print("Ada selisih MSE yang lumayan, artinya regularisasi (Ridge) ngasih")
    print("perbaikan performa dibanding Linear Regression biasa.")
    