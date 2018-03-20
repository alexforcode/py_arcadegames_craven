file = open('sources/example_sorted_names.txt')

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

# линейный поиск в массиве
pos = 0
while pos < len(name_list) and name_list[pos] != 'Auran':
    pos += 1

if pos == len(name_list):
    print('Имя не найдено.')
else:
    print('Имя находится в ячейке', pos)