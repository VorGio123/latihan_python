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

plt.show()

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