import re

part1_password = 0
part2_password = 0

# with open('/Users/jeremy/adventofcode/day3_input.txt', mode='r') as f:
with open('/Users/jeremy/adventofcode/DAY_3/day3_input.txt', mode='r') as f:
    # summed_total = 0
    for line in f:
        digit_list = list(line.strip())
        p1_first_number = max(digit_list[:-1])
        p1_first_index = digit_list[:-1].index(p1_first_number)
        p1_second_number = max(digit_list[p1_first_index + 1:])
        # print(f'{first_number}{second_number}')
        part1_password = part1_password + int(f'{p1_first_number}{p1_second_number}')
    print(f'part 1 password : {part1_password}')
        
# with open('/Users/jeremy/adventofcode/DAY_3/day3_edge.txt', mode='r') as f:
#     summed_total = 0
#     for line in f:
#         print(line)
#         line_total = ''
#         digit_list = list(line.strip())
#         # print(digit_list)
#         length_required = -11
#         # print(digit_list[:length_required])
#         max_num = max(digit_list[:length_required])
#         # print(max_num)
#         m_index = digit_list.index(max_num)
#         # print(m_index)
#         shrunk_list = digit_list[m_index+1:]
#         # print(shrunk_list)
#         line_total = line_total + max_num
#         while length_required < -1:
#             length_required +=1
#             max_num = max(shrunk_list[:length_required]) 
#             m_index = shrunk_list.index(max_num)
#             # print(max_num)
#             line_total = line_total + max_num
#             shrunk_list = shrunk_list[m_index+1:] 
#             # print(shrunk_list)
#         if length_required == -1:
#             max_num = max(shrunk_list)
#             line_total = line_total + max_num
#         print(line_total)
#         summed_total = summed_total + int(line_total)
#     print(summed_total)

with open('/Users/jeremy/adventofcode/DAY_3/day3_input.txt', mode='r') as f:
    summed_total = 0
    for line in f:
        line_total = ''
        length_required = -11

        digit_list = list(line.strip())
        total_length = len(digit_list)
        
        max_num = max(digit_list[:len(digit_list)+length_required])
        m_index = digit_list.index(max_num)
        shrunk_list = digit_list[m_index+1:]
        line_total = line_total + max_num

        while length_required < -1:
            length_required +=1
            max_num = max(shrunk_list[:len(shrunk_list)+length_required]) 
            m_index = shrunk_list.index(max_num)
            line_total = line_total + max_num
            shrunk_list = shrunk_list[m_index+1:] 

        # GET LAST NUMBER
        if length_required == -1:
            max_num = max(shrunk_list)
            line_total = line_total + max_num

        print(line_total)
        summed_total = summed_total + int(line_total)
    print(f'part 2 password : {summed_total}')