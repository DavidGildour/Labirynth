SYMBOLS = '0123456789abcdefghijklmnopqrstuvwyz'
from math import sqrt
from random import randrange

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

    def pick_neighbour(self, grid):
        neighbors = []
        size = int(sqrt(len(grid)))
        i = self.i
        j = self.j
        if not self.walls["top"] and not grid[i + (j - 1) * size].visited:
            neighbors.append(grid[i + (j - 1) * size])
        if not self.walls["right"] and not grid[(i + 1) + j * size].visited:
            neighbors.append(grid[(i + 1) + j * size])
        if not self.walls["bottom"] and not grid[i + (j + 1) * size].visited:
            neighbors.append(grid[i + (j + 1) * size])
        if not self.walls["left"] and not grid[(i - 1) + j * size].visited:
            neighbors.append(grid[(i - 1) + j * size])

        if len(neighbors) > 0:
            r = randrange(0, len(neighbors))
            return neighbors[r]
        else:
            return None

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
