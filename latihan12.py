#summary function
import pandas as pd

data = {
    "Nama": ["Andi", "Budi", "Citra", "Doni"],
    "Nilai": [80, 75, 90, 60],
    "Umur": [17, 18, 19, 17]
}

df = pd.DataFrame(data)

print(df)

#describe
print("\n===== Ringkasan Statistik =====")
print(df.describe())

#mean
print("\n===== Rata-rata Nilai =====")
print(df["Nilai"].mean())

#sum
print("\n===== Jumlah Nilai =====")
print(df["Nilai"].sum())

#min
print("\n===== Nilai Terkecil =====")
print(df["Nilai"].min())

#max
print("\n===== Nilai Terbesar =====")
print(df["Nilai"].max())

#value_counts
print("\n===== Jumlah Kemunculan Umur =====")
print(df["Umur"].value_counts())

#uniqe
print("\n===== Umur yang Unik =====")
print(df["Umur"].unique())

#map
kategori = {
    90: "Sangat Baik",
    80: "Baik",
    75: "Baik",
    60: "Cukup"
}

df["Kategori"] = df["Nilai"].map(kategori)

print("\n===== Data Setelah Ditambah Kategori =====")
print(df)

#apply
def status_lulus(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"

df["Status"] = df["Nilai"].apply(status_lulus)

print("\n===== Status Kelulusan =====")
print(df)