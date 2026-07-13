#NUMPY#
#import numpy
import numpy

array = numpy.array([1, 2, 3])
print(array)

#impor numpy as np#
import numpy as np

array = np.array([1, 2, 3])
print(array)

#from math import sqrt#
import math

print(math.sqrt(16))

#import semua fungsi
from math import *

print(sqrt(49))

#dokumentasi library
import numpy

help(numpy.array)


#numpy as np#
import numpy as np

arr = np.array([1, 2, 3, 4])
squared = arr ** 2

print(squared)

#PANDAS
#panda as pd
import pandas as pd

data = {
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Usia': [25, 30, 35]
}

df = pd.DataFrame(data)

print(df)
print(df['Nama'])

#MATPLOTIB
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)
plt.show()