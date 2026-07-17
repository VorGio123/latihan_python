#menggabungkan konsep
import pandas as pd

data = {
    "Produk": ["Laptop", "Smartphone", "Tablet"],
    "Harga": [1200, 800, 400],
    "Stok": [15, 50, 20]
}

df = pd.DataFrame(data, index=["Barang1", "Barang2", "Barang3"])

print(df)

#mengakses series
harga_series = df["Harga"]

print(harga_series)

#melihat ukuran data
print(df.shape)

#menampilkan baris awal
print(df.head(2))