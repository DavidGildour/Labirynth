SYMBOLS = '0123456789abcdefghijklmnopqrstuvwyz'
from math import sqrt

def move(pos, dirs, dir, grid):
	i = SYMBOLS.index(pos[0])
	j = SYMBOLS.index(pos[1])
	size = int(sqrt(len(grid)))
	if dir in dirs.values():
		if dir == dirs['up'] and pos == '00':
			return 'win'
		elif dir == dirs['up'] and grid[i + j * size].walls["top"] != True:
			j -= 1
		elif dir == dirs['down'] and grid[i + j * size].walls["bottom"] != True:
			j += 1
		elif dir == dirs['left'] and grid[i + j * size].walls["left"] != True:
			i -= 1
		elif dir == dirs['right'] and grid[i + j * size].walls["right"] != True:
			i += 1
	pos = SYMBOLS[i] + SYMBOLS[j]
	return pos
