def foo(level):
    print('Recursion call. Level:', level)
    if level < 10:
        foo(level+1)

foo(1)