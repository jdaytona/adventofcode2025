import os

all             = list(range(100))
current         = all[50]
list_item_count = len(all)
# total_zero      = 0


def return_current(direction, count, current_num):
    if direction == 'R':
        while current_num + count >= list_item_count:
            count = count - list_item_count
        return current_num + count
    if direction == 'L':
        while current_num - count < 0:
            count = count - list_item_count
        return current_num - count


with open('/Users/jeremy/adventofcode/DAY_1/day1_part1.txt', mode='r') as f:
    total_zero = 0
    for line in f:
        direction   = line[0]
        count       = int(line[1:])   
        current     = return_current(direction, count, current)
        # print(direction, count)
        
        # if current == 0:
        print(current)
        if current == 0:
            total_zero += 1


print(total_zero)

    