#sebelum menggunakan
import pandas as pd

print("\n===== Data Sebelum Rename =====")

data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
}

df = pd.DataFrame(data)

print(df)

#setelah menggunakan
print("\n===== Data Setelah Rename =====")

df.rename(
    columns={
        "A": "Alpha",
        "B": "Beta",
        "C": "Gamma"
    },
    inplace=True
)

print(df)

#menggantikan nama kolom
print("\n===== Mengganti Semua Nama Kolom =====")

df.columns = ["Nama", "Umur", "Kota"]

print(df)

#praktik asli
print("\n===== Contoh Rename Pada Data Asli =====")

data = {
    "f1": [25, 30, 35],
    "f2": [50000, 60000, 70000],
    "f3": ["L", "P", "L"]
}

df = pd.DataFrame(data)

print("Sebelum Rename")
print(df)

#rename
print("\n===== Setelah Rename =====")

df.rename(
    columns={
        "f1": "Usia",
        "f2": "Pendapatan",
        "f3": "Jenis Kelamin"
    },
    inplace=True
)

print(df)

#menggabungkan dataframe (concat)
print("\n===== Menggabungkan DataFrame dengan concat() =====")

df1 = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

df2 = pd.DataFrame({
    "A": [5, 6],
    "B": [7, 8]
})

print("DataFrame 1")
print(df1)

print("\nDataFrame 2")
print(df2)

#hasil concat
print("\n===== Hasil concat() =====")

hasil = pd.concat([df1, df2], axis=0)

print(hasil)

#menggabungkan dataframe (merge)
print("\n===== Menggabungkan DataFrame dengan merge() =====")

df1 = pd.DataFrame({
    "Kunci": ["K1", "K2"],
    "A": [1, 2]
})

df2 = pd.DataFrame({
    "Kunci": ["K1", "K2"],
    "B": [3, 4]
})

print("DataFrame 1")
print(df1)

print("\nDataFrame 2")
print(df2)

#hasil merge
print("\n===== Hasil merge() =====")

hasil = pd.merge(df1, df2, on="Kunci", how="inner")

print(hasil)

#menggabungkan dataframe (join)
print("\n===== Menggabungkan DataFrame dengan join() =====")

df1 = pd.DataFrame({
    "Nama": ["Andi", "Budi", "Citra"]
})

df2 = pd.DataFrame({
    "Nilai": [90, 85, 95]
})

print("DataFrame 1")
print(df1)

print("\nDataFrame 2")
print(df2)

#hasil join
print("\n===== Hasil join() =====")

hasil = df1.join(df2)

print(hasil)