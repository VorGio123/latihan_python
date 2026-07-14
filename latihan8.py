#probalitas dasar
import numpy as np

np.random.seed(0)

throws = np.random.randint(1, 7, size=10000)

even_count = np.sum(throws % 2 == 0)

probability_even = even_count / len(throws)

print(probability_even)

#probalitas bersyarat
import numpy as np

np.random.seed(0)

throws = np.random.randint(1, 7, size=10000)

lebih_dari_3 = throws > 3

genap = throws % 2 == 0

probability = np.sum(lebih_dari_3 & genap) / np.sum(lebih_dari_3)

print(probability)

#indepensi kejadian
import numpy as np

np.random.seed(0)

coin = np.random.choice(["Kepala", "Ekor"], size=10)

dice = np.random.randint(1, 7, size=10)

print("Koin:")
print(coin)

print("\nDadu:")
print(dice)

#kovariansi
import numpy as np

jam_belajar = np.array([1, 2, 3, 4, 5])

nilai = np.array([60, 70, 80, 90, 100])

cov = np.cov(jam_belajar, nilai)

print(cov)

#distribusi uniform
import numpy as np

np.random.seed(0)

uniform_data = np.random.uniform(0, 10, 10)

print(uniform_data)

#distribusi binomial
import numpy as np

np.random.seed(0)

hasil = np.random.binomial(n=10, p=0.5, size=10)

print(hasil)

#distribusi poison
import numpy as np

np.random.seed(0)

data = np.random.poisson(lam=5, size=10)

print(data)

#distibusi normal
import numpy as np

np.random.seed(0)

data = np.random.normal(loc=50, scale=10, size=10)

print(data)

#distribusi eksponensial
import numpy as np

np.random.seed(0)

data = np.random.exponential(scale=2, size=10)

print(data)

#hukum bilangan besar
import numpy as np

np.random.seed(0)

coin = np.random.choice([0,1], size=100000)

print(np.mean(coin))