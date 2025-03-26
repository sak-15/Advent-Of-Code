def count_word(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid_word(x,y):
        shape1 = False
        shape2 = False
        if(((x - 1 >= 0) and (y - 1 >= 0)) and ((x + 1 < rows) and (y + 1 < cols))):
            # Top right to bottom left
            if grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S":
                shape1 = True
            if grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M":
                shape1 = True
            # Top left to bottom right
            if grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S":
                shape2 = True
            if grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M":
                shape2 = True

        return shape1 and shape2
    
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "A":
                if is_valid_word(x,y):
                    count += 1
    return count

def load_grid():
    grid = []
    with open("input4.txt", "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

grid = load_grid()
count = count_word(grid)
print(count)