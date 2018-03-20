num_questions = 5
correct_answers = 0

print('Quiz time!')

print()
answer = int(input('How many books are there in the Harry Potter series?\n'))
if answer == 7:
    print('Correct!')
    correct_answers += 1
else:
    print('Wrong!')

print()
answer = int(input('What is 3*(2-1)?\n'))
if answer == 3:
    print('Correct!')
    correct_answers += 1
else:
    print('Wrong!')

print()
answer = int(input('What is 3*2-1?\n'))
if answer == 5:
    print('Correct!')
    correct_answers += 1
else:
    print('Wrong!')

print()
answer = int(input('''Who sings Black Horse and the Cherry Tree?
    1. Kelly Clarkson
    2. K.T. Tunstall
    3. Hillary Duff
    4. Bon Jovi\n'''))
if answer == 2:
    print('Correct!')
    correct_answers += 1
else:
    print('Wrong!')

print()
answer = int(input('''Who is on the front of a one dollar bill?
    1. George Washington
    2. Abraham Lincoln
    3. John Adams
    4. Thomas Jefferson\n'''))
if answer == 1:
    print('Correct!')
    correct_answers += 1
else:
    print('Wrong!')

print()
print('Congratulations, you got {} answers right.'.format(correct_answers))
print('That is a score of {} percent.'.format(correct_answers * 100 / num_questions))