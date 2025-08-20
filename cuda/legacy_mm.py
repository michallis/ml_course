import numpy as np
import random
import time

from pycparser.ply.yacc import resultlimit


def mm(matrix1, matrix2):
    result = []
    for i, row in enumerate(matrix1):
        newRow = []
        for j, col in enumerate(row):
            dot_product = sum(matrix1[i][i] * matrix2[k][j] for k in range(0, len(matrix2)))
            newRow.append(dot_product)
        result.append(newRow)
    return result

# generate square matrix
def create_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

start_time = time.monotonic()

N = 1024

a = create_matrix(N)
b = create_matrix(N)

C = mm(a, b)
print(C)

end_time = time.monotonic()

print(end_time - start_time)



