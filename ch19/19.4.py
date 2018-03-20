# Factorials

# I - no recursion

def factorialNorec(n):
    answer = 1
    for i in range(2, n+1):
        print( i,"*",answer,"=", i*answer)
        answer *= i
    return answer

print("I can calculate a factorial!")
n = int(input("Enter a number: "))
answer = factorialNorec(n)
print(answer)

# II - with recursion

def factorialRec(n):
    if n == 1:
        return n
    else:
        x = factorialRec(n-1)
        print( n, "*", x, "=", n * x )
        return n * x

print("I can calculate a factorial!")
n = int(input("Enter a number: "))
answer = factorialRec(n)
print(answer)