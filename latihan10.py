#dictionary
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35],
    "Kota": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

print(df)

# Menyimpan ke CSV
df.to_csv("output.csv", index=False)

# Menjadikan kolom Nama sebagai index
df.set_index("Nama", inplace=True)

# Mengambil data Alice
print(df.loc["Alice"])

#filtering data
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35]
}

df = pd.DataFrame(data)

filtered_df = df[df["Umur"] > 30]

print(filtered_df)

#menambahkan kolom baru
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35]
}

df = pd.DataFrame(data)

# Menambah kolom baru
df["Nilai"] = [90, 85, 95]

print(df)

#menghapus kolom
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35],
    "Nilai": [90, 85, 95]
}

df = pd.DataFrame(data)

# Menghapus kolom Nilai
df = df.drop("Nilai", axis=1)

print(df)

#update data
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35]
}

df = pd.DataFrame(data)

df.loc[1, "Umur"] = 31

print(df)

#statistik dasar
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35]
}

df = pd.DataFrame(data)

print("Rata-rata :", df["Umur"].mean())
print("Terbesar  :", df["Umur"].max())
print("Terkecil  :", df["Umur"].min())
print("Jumlah    :", df["Umur"].sum())

#sorting
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35]
}

df = pd.DataFrame(data)

# Urut dari kecil ke besar
print(df.sort_values(by="Umur"))

print()

# Urut dari besar ke kecil
print(df.sort_values(by="Umur", ascending=False))

#dataframe
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, 30, 35]
}

df = pd.DataFrame(data)

print(df.info())

print()

print(df.describe())

#missing values
import pandas as pd
import numpy as np

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [25, np.nan, 35]
}

df = pd.DataFrame(data)

print("Data Asli")
print(df)

print("\nCek Data Kosong")
print(df.isnull())

print("\nIsi Data Kosong Menjadi 0")
print(df.fillna(0))

print("\nHapus Data Kosong")
print(df.dropna())

#membaca file csv
import pandas as pd

# Membaca file CSV yang sudah dibuat sebelumnya
df = pd.read_csv("output.csv")

# Menampilkan seluruh isi DataFrame
print("Isi DataFrame:")
print(df)

print()

# Menampilkan 5 baris pertama
print("5 Baris Pertama:")
print(df.head())