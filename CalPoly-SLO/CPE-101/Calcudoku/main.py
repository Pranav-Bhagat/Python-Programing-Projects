def main():
    grid = []
    for i in range(5):
        grid.append([0]*5)

    cage_input = read_input()
    
    i = 0
    checks = 0
    backtracks = 0
    while i < 25:
        grid[i/5][i%5] += 1
        checks += 1
       # print_grid(grid)
       # print ''
        if validate_all(grid,cage_input) and grid[i/5][i%5] <= 5:
            i += 1
        elif grid[i/5][i%5] <= 4:
            continue
        else:
            grid[i/5][i%5] = 0
            backtracks += 1
            i -= 1
   
    print '\n---Solution---\n' 
    print_grid(grid)
    print '\nchecks: {0:d} backtracks: {1:d}'.format(checks, backtracks)
   # print ('%s seconds' % (time.time() - start_time))
def read_input():
    input_data = []
    num_cages = int(raw_input("Number of cages: "))
    for i in range(num_cages):
        cage = raw_input("Cage number {0:d}: ".format(i)).split()
        cage = [int(i) for i in cage]
        input_data.append(cage)
    return input_data



def print_grid(grid):
    for i in range(len(grid)):
        print ' '.join(map(str, grid[i]))


def validate_rows(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i].count(j+1) > 1:
                return False 
    return True

def validate_cols(grid):
    col_grid = [] #transposing columns to rows
    for i in range(len(grid)):
        column = []
        for j in range(len(grid)):
            column.append(grid[j][i])
        col_grid.append(column) 
    return validate_rows(col_grid)

def validate_cages(grid, cages):
    for i in range(len(cages)):
        cage_sum = 0
        for j in range((cages[i][1])): # iterates n_cells times
            cell = cages[i][j+2] # selects current cell number
            grid_value = grid[(cell/(len(grid)))][(cell%(len(grid)))]
            cage_sum = cage_sum + grid_value     
            if grid_value <= 0:
                return True 
        if not cages[i][0] == cage_sum:
            return False
    return True

def validate_all(grid, cages):
    if validate_rows(grid) \
    and validate_cols(grid) \
    and validate_cages(grid,cages): 
        return True
    return False


if __name__ == "__main__":
    main()
