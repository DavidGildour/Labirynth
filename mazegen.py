"""TO DO:
ENHANCE MAZE GENERATING ALGORITHMS"""

from cell import Cell
from math import sqrt
#IN ORDER TO ENNUMERATE GRIDS LARGER THAN 9 I NEEDED TO EXPAND THE DIGITS
#'VOCABULARY'. SO NOW AFTER 9 THERE GOES ALL THE ALPHABET.
SYMBOLS = '0123456789abcdefghijklmnopqrstuvwyz'
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

def print_grid(grid, pos):
    """THIS IS ONLY FOR PRINTING THE GRID.
    DON'T MESS WITH THE GRID WITHIN THIS FUNCTION.
    """
    i = SYMBOLS.index(pos[0])
    j = SYMBOLS.index(pos[1])
    size = int(sqrt(len(grid)))
    #THIS REPLACES THE GIVEN CELL IN THE GRID (POS ARGUMENT) WITH '##'
    grid[i + j * size].row = '#'
    grid[i + j * size].col = '#'
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
            if cell.row == '#':
                print(cell.row + cell.col + VER_WALL, end = '')
            else:
                print('  ' + VER_WALL, end = '')
        else:
            if cell.row == '#':
                print(cell.row + cell.col + VER_PASSAGE, end = ' ')
            else:
                print('  ' + VER_PASSAGE, end = ' ')
        if cell.i + cell.j == (size - 1) * 2: # the last cell in a grid
            print('\n' + (CORNER + HOR_WALL) * (size - 1) + (CORNER + HOR_PASSAGE) + CORNER)
    #THIS REVERSES THE REPLACEMENT AT THE BEGINNING OF THE FUNCTION, THUS
    #ALLOWING TO REPLACE IT ONCE AGAIN WITHOUT LEAVING A TRACE
    grid[i + j * size].row = SYMBOLS[i]
    grid[i + j * size].col = SYMBOLS[j]

def mazegen(size):
    grid = []
    for j in range(size):
        for i in range(size):
            cell = Cell(i, j)
            grid.append(cell)
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
    return grid
