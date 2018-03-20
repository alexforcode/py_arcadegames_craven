# VII
'''def foo(n):
    if n == 1:
        return 6
    else:
        return foo(n-1)/2 + 4

for n in range(10):
    print('n =', n+1, ', a =', foo(n+1))'''

# VIII
def foo(n):
    while n < 11:
        if (n == 1) or (n == 2):
            return 1
        else:
            return foo(n-1) + foo(n-2)

for n in range(10):
    print(foo(n+1), end=' ')