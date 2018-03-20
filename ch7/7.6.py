months="JanFebMarAprMayJunJulAugSepOctNovDec"
try:
    n = int(input("Enter a month number: "))
    if (n > 12 or n < 0):
        print('Not in range!')
    else:
        print(months[(n*3-3):(n*3)])
except:
    print('Error!')