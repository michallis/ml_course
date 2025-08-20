from numba import cuda
import numpy as np
import math
import time

@cuda.jit
def matmul_kernal(A, B, C):
    sA = cuda.shared.array(shape=(TPB,TPB),dtype=np.float32)
    sB = cuda.shared.array(shape=(TPB,TPB),dtype=np.float32)
    x,y = cuda.grid(2)
    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bpg = cuda.gridDim.x

    if x >= C.shape[0] and y >= C.shape[1]:
        return

    tmp = 0
    for i in range(bpg):
        sA[tx,ty] = A[y, tx + i * TPB]
        sB[tx, ty] = A[ty + i * TPB, x]

        cuda.syncthreads()
        for j in range(TPB):
            tmp += sA[ty, j] * sB[j, tx]

        cuda.syncthreads()

    C[y,x] = tmp

N = 512
TPB = 32

start_time = time.monotonic()
A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)
C = np.zeros((N,N), dtype=np.float32)

threadperblock = (TPB,TPB)

blockspergrid_X = math.ceil(A.shape[0]/threadperblock[0])
blockspergrid_y = math.ceil(B.shape[1]/threadperblock[1])
blockspergrid = (blockspergrid_X, blockspergrid_y)

matmul_kernal[blockspergrid, threadperblock](A, B, C)

print(C)

end_time = time.monotonic()

print(end_time - start_time)




