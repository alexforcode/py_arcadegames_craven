def get_high_score():
    high_score = 0
    try:
        file = open('sources/high_score.txt', 'rb')
        high_score = int.from_bytes(file.read(), byteorder='big')  # int(file.read())
        file.close()
        print('High score:', high_score)
    except IOError:
        print('No high score yet.')
    except ValueError:
        print('Starting with no high score.')
    return high_score

def save_high_score(new_high_score):
    try:
        file = open('sources/high_score.txt', 'wb')
        file.write(new_high_score.to_bytes(4, byteorder='big', signed=True))
        file.close()
    except IOError:
        print('Unable to save the high score.')

def main():
    high_score = get_high_score()
    current_score = 0
    
    try:
        current_score = int(input('What is your score? '))
    except ValueError:
        print('Incorrect format. Not number.')
    
    if current_score > high_score:
        print('Congrats! New high score here!')
        save_high_score(current_score)
    else:
        print('Sorry. Better luck next time.')

if __name__ == '__main__':
    main()
