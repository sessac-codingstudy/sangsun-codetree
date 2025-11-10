a = input()

A = list(a)
A[1] = 'a'
A[-2] = 'a'
print(''.join(A))
