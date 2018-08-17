from symbols import SYMBOLS
from math import sqrt
from random import randrange

CORNER = '+'
HOR_WALL = ' -- '
LEFT_WALL = '| '
VER_WALL = ' | '
HOR_PASSAGE = '    '
VER_PASSAGE = '  '

def remove_walls(a, b):
    x = a.i - b.i
    if x == 1: # LEFT neighbor
        a.walls["left"] = False
        b.walls["right"] = False
    elif x == -1: # RIGHT neighbor
        a.walls["right"] = False
        b.walls["left"] = False

    y = a.j - b.j
    if y == 1: # TOP neighbor
        a.walls["top"] = False
        b.walls["bottom"] = False
    elif y == -1: # BOTTOM neighbor
        a.walls["bottom"] = False
        b.walls["top"] = False

def mazegen(grid):
    visited = []
    stack = []
    current = grid[0]
    print("Generating maze... ", end = '')
    while len(visited) != len(grid):
        if not current.visited:
            current.visited = True
            visited.append(current)
        next = current.check_neighbors(grid)
        if next:
            remove_walls(current, next)
            stack.append(current)
            current = next
        elif len(stack) > 0:
            current = stack.pop()
    print("Done!")


def print_grid(grid):
    size = int(sqrt(len(grid)))
    for cell in grid:
        indx = grid.index(cell)
        if cell.i + cell.j == 0: # the first cell in a grid
            print((CORNER + HOR_PASSAGE) + (CORNER + HOR_WALL) * (size - 1) + CORNER + '\n' + LEFT_WALL, end = '')
        elif cell.i == 0: # the first cell in a row (but not the first row)
            # printing horizontal walls
            print()
            for cell_in_row in grid[indx:indx + size]: # iterating over every cell in current row
                if cell_in_row.walls["top"] == True:
                    print(CORNER + HOR_WALL, end = '')
                else:
                    print(CORNER + HOR_PASSAGE, end = '')
            print(CORNER + '\n' + LEFT_WALL, end = '')
        # printing cells and vertical walls between
        if cell.walls["right"] == True:
            print('  ' + VER_WALL, end = '')
        else:
            print('  ' + VER_PASSAGE, end = ' ')
        if cell.i + cell.j == (size - 1) * 2: # the last cell in a grid
            print('\n' + (CORNER + HOR_WALL) * (size - 1) + (CORNER + HOR_PASSAGE) + CORNER)

class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.row = SYMBOLS[i]
        self.col = SYMBOLS[j]
        self.walls = {"top":    True,
                      "right":  True,
                      "bottom": True,
                      "left":   True}
        self.visited = False

    def check_neighbors(self, grid):
        size = int(sqrt(len(grid)))
        neighbors = []
        i = self.i
        j = self.j

        if j != 0: top = grid[i + (j - 1) * size]
        else: top = None
        if i != size - 1: right = grid[(i + 1) + j * size]
        else: right = None
        if j != size - 1: bottom = grid[i + (j + 1) * size]
        else: bottom = None
        if i != 0: left = grid[(i - 1) + j * size]
        else: left = None

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        if len(neighbors) > 0:
            r = randrange(0, len(neighbors))
            return neighbors[r]
        else:
            return None

def main():
    cells = []
    size = int(input("Size: "))

    for j in range(size):
        for i in range(size):
            cell = Cell(i, j)
            cells.append(cell)

    mazegen(cells)
    print_grid(cells)

if __name__ == '__main__':
    main()
