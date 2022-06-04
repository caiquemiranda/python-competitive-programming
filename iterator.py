# list test
L = [1, 2, 3, 4, 9, 6]

def all_pairs(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            yield (L[i], L[j])

