
def count_word(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    count = 0

    def checks(x,y,dx,dy):
        for i in range(len(word)):

            newX = x + i * dx
            newY = y + i * dy

            # Check if the new position is out of the grid
            if not ((0 <= newX < rows) and (0 <= newY < cols)):
                return False

            # Check if the letter is not the same
            if grid[newX][newY] != word[i]:
                return False
        return True



    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if checks(x,y,dx,dy):
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
