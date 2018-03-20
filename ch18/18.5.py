def getInput():
    userInput = input("Введите что-нибудь: ")
    if len(userInput) == 0:
        raise IOError("Пользователь ничего не ввёл")
     
try:
    getInput()
except IOError as e:
    print(e)