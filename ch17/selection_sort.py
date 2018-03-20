import random

def selection_sort(num_list):
    count_in = 0
    count_out = 0
    for cur_pos in range(len(num_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos+1, len(num_list)):
            if num_list[scan_pos] < num_list[min_pos]:
                min_pos = scan_pos
            count_in += 1
            print('In: ', count_in)
        if cur_pos != min_pos:
            temp = num_list[min_pos]
            num_list[min_pos] = num_list[cur_pos]
            num_list[cur_pos] = temp
        count_out += 1
        print('Out: ', count_out)

def print_list(num_list):
    for item in num_list:
        print(item, end=' ')
    print()

num_list = []
for i in range(15):
    num_list.append(random.randrange(100))

print_list(num_list)
selection_sort(num_list)
print_list(num_list)

