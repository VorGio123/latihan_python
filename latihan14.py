#tipe_data
import pandas as pd

data = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": ["20", "25", "30"],
    "Gaji": [5000000, 6000000, 7000000]
}

df = pd.DataFrame(data)

#data
print("===== Data Karyawan =====")
print(df)

#semua kolom
print("\n===== Tipe Data Semua Kolom (dtypes) =====")
print(df.dtypes)


#kolom umur
print("\n===== Tipe Data Kolom Umur (dtype) =====")
print(df["Umur"].dtype)

#kolom nama
print("\n===== Tipe Data Kolom Nama (dtype) =====")
print(df["Nama"].dtype)

#astype()
df ["Umur"] = df["Umur"].astype(int)

#astype(int)
print("\n===== Tipe Data Setelah astype(int)=====")
print(df.dtypes)

#setelah mengubah
print("\n===== Data Setelah Mengubah Tipe Data =====") 
print(df)

#convert_dtypes()
print("\n===== Mengubah Tipe Data Otomatis =====")

df = df.convert_dtypes()

print(df.dtypes)

#missing values
print("\n===== Contoh Data dengan Nilai Kosong =====")

data_kosong = {
    "Nama": ["Alice", "Bob", "Charlie"],
    "Umur": [20, None, 30],
    "Gaji": [5000000, 6000000, None]
}

df_kosong = pd.DataFrame(data_kosong)

print(df_kosong)

#menggecek nilai kosong
print("\n===== Mengecek Nilai Kosong (isnull) =====")
print(df_kosong.isnull())

#fillna()
print("\n===== Mengisi Nilai Kosong dengan 0 =====")

df_isi = df_kosong.fillna(0)

print(df_isi)

#dropna()
print("\n===== Menghapus Baris yang Memiliki Nilai Kosong =====")

df_hapus = df_kosong.dropna()

print(df_hapus)

# belum_memakai replace()
print("\n===== Data Sebelum replace() =====")

data_jk = {
    "Nama": ["Andi", "Budi", "Citra"],
    "JK": ["L", "L", "P"]
}

df_jk = pd.DataFrame(data_jk)

print(df_jk)

#sesudah_memakai replace()
print("\n===== Data Setelah replace() =====")

df_jk["JK"] = df_jk["JK"].replace({
    "L": "Laki-laki",
    "P": "Perempuan"
})

print(df_jk)