from symbols import SYMBOLS
SIZE = int(input("Size: "))
CORNER = '+'
HOR_WALL = ' -- '
VER_WALL = '| '
PASSAGE = '    '

class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.row = SYMBOLS[i]
        self.col = SYMBOLS[j]
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self):
        if cell.i + cell.j == 0: # the first cell at all
            print((CORNER + PASSAGE) + (CORNER + HOR_WALL) * (SIZE - 1) + CORNER)
        elif cell.i % SIZE == 0: # the first cell in a row (but not the first row)
            print(VER_WALL + '\n' + (CORNER + HOR_WALL) * SIZE + CORNER)
        print(VER_WALL + cell.row + cell.col, end = ' ')
        if cell.i + cell.j == (SIZE - 1) * 2: # the last cell
            print(VER_WALL + '\n' + (CORNER + HOR_WALL) * (SIZE - 1) + (CORNER + PASSAGE) + CORNER)

cells = []

for j in range(SIZE):
    for i in range(SIZE):
        cell = Cell(i, j)
        cells.append(cell)

for cell in cells:
    cell.show()
