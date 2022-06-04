# start

# list base tests
L = [1, 2, 3, 4, 9, 2, 1, 4, 2, 6]


# returno a sorted copy of the list
print(sorted(L)) # O(n log n)
print(L)

# sorts in place
L.sort() # O(n log n)
print(L)


# scructure data
# dict, set, list, tuple
L2 = list(range(10))
print(L2)

L3 = '-'.join(['A', 'B', 'C'])
print(L3)