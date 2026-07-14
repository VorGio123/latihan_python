#matriks
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A)

#determinan matriks
import numpy as np

B = np.array([
    [4, 2],
    [3, 1]
])

det_B = np.linalg.det(B)

print(det_B)

#penjumlahan matriks
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A + B

print(C)

#perkalian matriks
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = np.dot(A, B)

print(C)

#matriks invers
import numpy as np

A = np.array([
    [4, 7],
    [2, 6]
])

A_inv = np.linalg.inv(A)

print(A_inv)

#transpos matriks
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

A_transpose = A.T

print(A_transpose)

#vektor
import numpy as np

vektor = np.array([10, 20, 30])

print(vektor)

#ketergantungan linier(Liniear Dependence)
import numpy as np

vektor = np.array([10, 20, 30])

print(vektor)

#rank matriks
import numpy as np

A = np.array([
    [1, 2],
    [2, 4]
])

rank = np.linalg.matrix_rank(A)

print(rank)

#Eigenvalue & Eigenvector
import numpy as np

A = np.array([
    [4, 2],
    [1, 3]
])

eigenvalue, eigenvector = np.linalg.eig(A)

print("Eigenvalue:")
print(eigenvalue)

print("\nEigenvector:")
print(eigenvector)