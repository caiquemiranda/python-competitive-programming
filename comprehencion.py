# list and Dictionary Comprehension,

n = 5
square_numbers = [x**2 for x in range(n)]
print(square_numbers)


t= [0 for _ in range(n)]
print(t)


my_string = 'cowboy bebop'

nb_occurrences = {letter: 0 for letter in my_string}
print(nb_occurrences)

'''
nb_occurrences = {}
for letter in my_string:
    nb_occurrences[letter] = 0
print(nb_occurrences)
'''

