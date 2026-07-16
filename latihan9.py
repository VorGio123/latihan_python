#fungsi linear
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = 2 * x + 1

plt.plot(x, y, label="f(x)=2x+1")
plt.title("Linear Function")
plt.legend()
plt.show()

#fungsi kuadrat
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = x**2 + 5

plt.plot(x, y, label='f(x)=x²-4x+3')
plt.title("Quadratic Function")
plt.legend()

# plt.show()

#fungsi polinomial
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = 0.1 * x**3 - 0.5 * x**2 + 2 * x - 1

plt.plot(x, y, label="f(x) = 0.1x³ - 0.5x² + 2x - 1")
plt.title("Polynomial Function")
plt.legend()

plt.show()

#fungsi eksponensial
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = 2**x

plt.plot(x, y, label="f(x) = 2^x")
plt.title("Exponential Function")
plt.legend()

plt.show()

#fungsi logaritmik
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 400)
y = np.log(x)

plt.plot(x, y, label='f(x) = log(x)')
plt.title('Logarithmic Function')
plt.legend()

plt.show()

#fungsi trigonometri
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = np.sin(x)

plt.plot(x, y, label='f(x) = sin(x)')
plt.title('Trigonometric Function')
plt.legend()

plt.show()

#turunan(derivative)
import numpy as np
import matplotlib.pyplot as plt

## Fungsi asli
def f(x):
    return 3 * x**3 - 6 * x**2 + x - 4

## Turunan pertama
def first_derivative(x):
    return 9 * x**2 - 12 * x + 1

## Turunan kedua
def second_derivative(x):
    return 18 * x - 12

## Membuat nilai x
x = np.linspace(-2, 4, 400)

## Membuat grafik
plt.plot(x, f(x), label='f(x)')
plt.plot(x, first_derivative(x), label="f'(x)")
plt.plot(x, second_derivative(x), label="f''(x)")

## Judul dan keterangan
plt.title("Derivatives of a Polynomial Function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

## Menampilkan grafik
plt.show()

#gradient descent
import numpy as np
import matplotlib.pyplot as plt

# Fungsi
def f(x):
    return x**2

# Turunan fungsi
def grad(x):
    return 2 * x

# Nilai awal
x = 4

# Learning rate (besar langkah)
learning_rate = 0.1

# Menyimpan perjalanan titik
history = [x]

# Proses Gradient Descent
for i in range(20):
    x = x - learning_rate * grad(x)
    history.append(x)

# Membuat grafik
x_plot = np.linspace(-5, 5, 400)
y_plot = f(x_plot)

plt.plot(x_plot, y_plot, label="f(x)=x²")
plt.scatter(history, f(np.array(history)), color="red", label="Gradient Descent")

plt.title("Gradient Descent")
plt.legend()
plt.grid(True)

plt.show()

#integral
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Fungsi
def f(x):
    return x**2

# Menghitung integral dari 0 sampai 2
hasil, error = quad(f, 0, 2)

print("Hasil Integral =", hasil)

# Membuat grafik
x = np.linspace(0, 2, 400)
y = f(x)

plt.plot(x, y, label="f(x)=x²")
plt.fill_between(x, y, alpha=0.3, label="Luas Integral")

plt.title("Integral")
plt.legend()
plt.grid(True)

plt.show()