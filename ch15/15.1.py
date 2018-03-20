file = open('sources/example_sorted_names.txt')

for line in file:
    line = line.strip()
    print(line)

file.close()