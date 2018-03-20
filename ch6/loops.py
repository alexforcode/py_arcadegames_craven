# I
'''for col in range(10):
    print('*', end=' ')'''

# II
'''for col in range(10):
    print('*', end=' ')
print()
for col in range(5):
    print('*', end=' ')
print()
for col in range(20):
    print('*', end=' ')'''

# III
'''for row in range(10):
    for col in range(10):
        print('*', end=' ')
    print()'''

# IV
'''for row in range(10):
    for col in range(5):
        print('*', end=' ')
    print()'''

# V
'''for row in range(5):
    for col in range(20):
        print('*', end=' ')
    print()'''

# VI
'''for time in range(10):
    for num in range(10):
        print(num, end=' ')
    print()'''

# VII
'''for time in range(10):
    for num in range(10):
        print(time, end=' ')
    print()'''

# VIII
'''for time in range(10):
    for num in range(time+1):
        print(num, end=' ')
    print()'''

# IX
'''for time in range(10):
    for space in range(time):
        print(' ', end=' ')
    for num in range(10-time):
        print(num, end=' ')
    print()'''

# X
'''for mult in range(1, 10):
    for base in range(1, 10):
        if base*mult < 10:
            print(' ', end='')
        print(base*mult, end=' ')
    print()'''

# XI
'''print()
for i in range(1, 10):
    for j in range(10-i):
        print(' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(i-1, 0, -1):
        print(j, end=' ')      
    print()'''

# XII
'''print()
for i in range(1, 10):
    for j in range(10-i):
        print(' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(i-1, 0, -1):
        print(j, end=' ')      
    print()
for i in range(1, 9):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(1, 10-i):
        print(j, end=" ")
    print()'''

# XIII
print()
for i in range(1, 10):
    for j in range(10-i):
        print(' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(i-1, 0, -1):
        print(j, end=' ')      
    print()
for i in range(10):
    for j in range(i+2):
        print(' ', end=' ')
    for j in range(1, 9-i):
        print(j, end=' ')
    for j in range(7-i, 0, -1):
        print(j, end=' ')
    print()