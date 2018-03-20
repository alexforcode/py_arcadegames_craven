def searchName(name_list, name):
    pos = 0
    while pos < len(name_list) and name_list[pos] != name:
        pos += 1

    if pos == len(name_list):
        return -1
    else:
        return pos

file = open('sources/example_sorted_names.txt')

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

print(searchName(name_list, 'Alex'))