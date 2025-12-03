import os

ALL             = list(range(100))
LIST_ITEM_COUNT = len(ALL)
# total_zero      = 0


def return_current(direction, count, old_current):
    loop_count = 0
    new_current = None
    if direction == 'R':
        while old_current + count >= LIST_ITEM_COUNT:
            count = count - LIST_ITEM_COUNT
            loop_count += 1
        new_current = old_current + count
    if direction == 'L':
        while old_current - count < 0:
            count = count - LIST_ITEM_COUNT
            loop_count += 1
        new_current = old_current - count
    if new_current == 0 and loop_count > 0 and direction == 'R':
        loop_count = loop_count - 1
    if old_current == 0 and loop_count > 0 and direction == 'L':
        loop_count = loop_count - 1
    return(new_current, loop_count)


with open('/Users/jeremy/adventofcode/DAY_1/day1_part1.txt', mode='r') as f:
# with open('day1_edge.txt', mode='r') as f:
    total_zero      = 0
    loop_counter    = 0
    current         = ALL[50]
    for line in f:
        direction               = line[0]
        count                   = int(line[1:])   
        current, loop_count     = return_current(direction, count, current)
        loop_counter = loop_counter + loop_count
        if current == 0:
            total_zero += 1
        print(f'{total_zero} {current} {loop_count} {total_zero + loop_counter} {direction} {count}')


print(total_zero + loop_counter)
# print(total_zero) # + 
# print(loop_counter)

    