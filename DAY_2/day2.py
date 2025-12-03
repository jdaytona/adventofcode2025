import re

with open('/Users/jeremy/adventofcode/DAY_2/day2_input.txt', mode='r') as f:
# with open('day2_edge.txt', mode='r') as f:
    part1_password = 0
    part2_password = 0
    for line in f:
        all_input_ranges = line.split(',')

        for spec_range in all_input_ranges:
            min_num = int(spec_range.split('-')[0])
            max_num = int(spec_range.split('-')[1])
            # print(f'min{min_num} max{max_num}')
            list_of_ranges = list(range(min_num, max_num + 1))
            for i in list_of_ranges:
                # print(type(i))
                si = str(i)
                x = re.search(r"\b(\d+)\1+\b", str(i))
                if len(si) % 2 == 0:
                    f_half, s_half = si[:len(si)//2], si[len(si)//2:]
                    if x and f_half == s_half:
                        part1_password = part1_password + int(x.string)
                if x:
                    print(x.string) 
                    part2_password = part2_password + int(x.string)
    print(f'part1_password: {part1_password}')
    print(f'part2_password: {part2_password}')
