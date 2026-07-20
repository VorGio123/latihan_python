#grouby
import pandas as pd

data = {
    "Nama": ["Andi", "Budi", "Citra", "Doni", "Eko"],
    "Kelas": ["A", "B", "A", "B", "A"],
    "Nilai": [80, 75, 90, 60, 70]
}

df = pd.DataFrame(data)

print(df)

#groupy_sum
group = df.groupby("Kelas")["Nilai"].sum()

print("\n===== Total Nilai Tiap Kelas =====")
print(group)

#agg
hasil = df.groupby("Kelas")["Nilai"].agg(["sum", "mean"])

print("\n===== Total dan Rata-rata Nilai =====")
print(hasil)

#groupy_kolom
import pandas as pd

data = {
    "Nama": ["Andi", "Budi", "Citra", "Doni", "Eko"],
    "Kelas": ["A", "B", "A", "B", "A"],
    "JK": ["L", "L", "P", "L", "L"],
    "Nilai": [80, 75, 90, 60, 70]
}

df = pd.DataFrame(data)

hasil = df.groupby(["Kelas", "JK"])["Nilai"].sum()

print(hasil)

#reset_index
hasil = df.groupby(["Kelas", "JK"])["Nilai"].sum()

print("Sebelum reset_index():")
print(hasil)

hasil = hasil.reset_index()

print("\nSetelah reset_index():")
print(hasil)

#sort_values
print("\n===== Urut Nilai (Kecil → Besar) =====")
print(df.sort_values("Nilai"))
#kebalikannya
print("\n===== Urut Nilai (Besar → Kecil) =====")
print(df.sort_values("Nilai", ascending=False))