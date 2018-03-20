file = open('sources/example_sorted_names.txt')

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

for name in name_list:
    print(name)