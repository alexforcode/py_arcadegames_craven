import random

def insertion_sort(num_list):
    count_out = 0
    count_in = 0 
    for key_pos in range(1, len(num_list)):
        key_value = num_list[key_pos]  # 21
        scan_pos = key_pos - 1         # 1
        while (scan_pos >= 0) and (num_list[scan_pos] > key_value):
            num_list[scan_pos+1] = num_list[scan_pos]
            scan_pos -= 1
            count_in += 1
            print('In: ', count_in)
        num_list[scan_pos+1] = key_value
        count_out += 1
        print('Out: ', count_out)

def print_list(num_list):
    for item in num_list:
        print(item, end=' ')
    print()

num_list = []
for i in range(10):
    num_list.append(random.randrange(100))

print_list(num_list)
insertion_sort(num_list)
print_list(num_list)