# I
'''def f():
    return 10
x = f()
print(x)'''

# II
'''def f(x):
    x += 10
    return x
x = 10
f(x)
print(x)'''

# III
'''def f(x):
    x += 10
    return x
def g(x):
    return x * 2
print(f(g(10)))'''

# IV
'''def f(x):
    x += 10
    return x
def g(x):
    return x * 2
print(g(f(10)))'''

# V
'''def f(x, y):
    return x / y
x = 20
y = 5
print(f(y, x))'''

# VI
'''def f(x):
    return x*2
def g(x):
    return x-2
def h(x):
    return x+10
print(f(5) + g(f(5)) + h(g(10)))
print(h(g(f(10))))'''

# VII
'''x=len([2,3,[5,6],[7,9]])
print(x)'''

# VIII
'''def hello():
    print('Hello')
# IX
hello()'''

#X
'''def spaceTotal(string):
    total = 0
    for char in string:
        if char == ' ':
            total += 1
    return total
print(spaceTotal('asd qwe asd asd'))'''

# XI
'''def printList(my_list):
    for item in my_list:
        print(item)
printList([10, 18, 5, -8, 3])'''

# XII
'''def sumList(my_list):
    total = 0
    for item in my_list:
        total += item
    return total
print(sumList([10, 18, 5, -8, 3]))'''