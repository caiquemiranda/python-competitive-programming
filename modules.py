import math
from math import sqrt

# print(sqrt(49))
# print(math.sqrt(49))


import tryalgo

# help(tryalgo)             list of modules
# help(tryalgo.arithm)      for a particular module

# err
# c = {}
# c['a'] += 1               the key does not exist
# print(c)                  err

# corr
# c['a'] = 1
# c['a'] += 1               now it does
# c['a'] += 3
# print(c)                  value correct

from collections import Counter

# c = Counter()
# c['a'] += 1               the key does not exist, so it so created
#print(c)
   
# c = Counter('cowboy bebop')
# print(c)

from collections import defaultdict

g = defaultdict(list)
g['paris'].append('marseille')  # 'paris' key is created
g['paris'].append('lion')
print(g)

print(g['paris'])










