# outputs clean

i_test = 1
answer = 1.2142

#1
print('Case #%d: %.2f gigawatts!! #1' % (i_test, answer))

#2
print('Case #{}: {:.2f} gigawatts!! #2'.format(i_test, answer))

#3
print(f'Case #{i_test}: {answer:.2f} gigawatts!! #3')

#4
precision = 2 
print(f'Case #{i_test}: {answer:.{precision}f} gigawatts!! #4')
