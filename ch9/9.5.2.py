# I
'''def sum(a,b,c):
    return (a+b+c)

print (sum(10,11,12))'''

# II
'''def increase(x):
    return x+1
 
x=10
print ("X is",x," I will now increase x." )
x = increase(x)
print ("X is now",x)'''

# III
'''def print_hello():
    print ("Hello")
 
print_hello()'''

# IV
'''def count_to_ten():
    for i in range(10):
        print(i+1)
 
count_to_ten()'''

# V
'''def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum
 
list = [45,2,10,-5,100]
print (sum_list(list))'''

# VI
'''def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result += text[(i+1)*-1]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))'''

# VII
'''def get_user_choice():
    while True:
        command = input("Command: ")
        if command=='f' or command=='m' or command=='s' or command=='d' or command=='q':
            return command
        print ("Hey, that's not a command. Here are your options:" )
        print ("f - Full speed ahead")
        print ("m - Moderate speed")
        print ("s - Status")
        print ("d - Drink")
        print ("q - Quit")
 
user_command = get_user_choice()
print("You entered:",user_command)'''