# PART 1
# 
# import sys
# sys.setrecursionlimit(100000)

grid = []
# directions does not include current location [0, 0]
directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]


def get_neighbors(input_grid, total_count):
      # print(grid[1][3])
    grid_rows       = len(input_grid)
    grid_columns    = len(input_grid[0])

    grid_row_range      = list(range(grid_rows))
    grid_column_range   = list(range(grid_columns))
    count = 0
    new_grid = input_grid[:]
    roles_to_remove = []

    for row in grid_row_range:
        for column in grid_column_range:
            lookup_item = '@'
            neighbors = []
            current = input_grid[row][column] 
            for dr, dc in directions:
                n_row, n_col = row + dr, column + dc                  
                if 0 <= n_row < grid_rows and 0 <= n_col < grid_columns:
                        if current == lookup_item:
                            neighbors.append(input_grid[n_row][n_col])
            if neighbors and neighbors.count(lookup_item) < 4:
                roles_to_remove.append(f'{row}:{column}')
                count += 1
    total_count += count
    return grid, total_count, count, roles_to_remove


# with open('/Users/jeremy/adventofcode2025/DAY_4/day4_edge.txt', mode='r') as f:
with open('/Users/jeremy/adventofcode2025/DAY_4/day4_input.txt', mode='r') as f:
    part1_total_count = 0
    part2_total_count = 0
    roles_to_remove = []
    new_grid = []
    grid = []
    count = 0
    total_count = 0
    for line in f:
        grid.append(list(line.strip()))

    new_grid, part1_total_count, count, roles_to_remove = get_neighbors(grid, part1_total_count)
    print(f'PART 1 - ToTAL COUNT : {part1_total_count}')
    new_grid, part2_total_count, count, roles_to_remove = get_neighbors(grid, part2_total_count)
    
    while count:
        for i in roles_to_remove:
            x = int(i.split(':')[0])
            y = int(i.split(':')[1])
            new_grid[x][y] = '.'
        new_grid, part2_total_count, count, roles_to_remove = get_neighbors(new_grid, part2_total_count)
    print(f'PART 2 - ToTAL COUNT : {part2_total_count}')
