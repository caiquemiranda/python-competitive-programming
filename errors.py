# frequent errors

from concurrent.futures import process


A = [1, 2, 3]
B = A                 # beware! both variables refer to same object

# corr
B = A[:]              # B becomes a distinct copy of A

M = [[0] * 10] * 10   # Do no write this

M1 = [[0] * 10 for _ in range(10)]
M2 = [[0 for j in range(10)] for i in range(10)]



# ranges

for i in range(0, 10):  # 0 included, 10 excluded
    process(A[i])


for i in range(9, -1, -1): # 9 included, -1 excluded
    process(A[i])


