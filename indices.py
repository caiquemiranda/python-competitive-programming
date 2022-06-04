# list base tests
L = [1, 2, 3, 4, 9, 6]
dic = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 9: 'e', 6: 'j'}


for index in range(len(L)):
    value = L[index]
    #  ... handlinng of index and value
    print(index, value)


for index, value in enumerate(L):
    #  ... handlinng of index and value
    print(index, value)


# dict
for key, value in dic.items():
    #  ... handlinng of key and value
    print(key, value)