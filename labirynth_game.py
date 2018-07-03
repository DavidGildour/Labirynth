from mazegen import *
from mvmnt_control import move
from sys import argv
#MODE '0' - WITHOUT GRID ENNUMERATION VISIBLE
#MODE '1' (OR ANYTHING ELSE THAN 0 ACTUALLY) - WITH GRID ENNUMERATION VISIBLE
try:
    script, mode = argv
except:
    mode = 1

#DEFAULT VALUES
dirs = {
    'up': 'u',
    'down': 'd',
    'left': 'l',
    'right': 'r'
}
size = 5
start = None

flag, size, dirs = getmenu(size, dirs)

grid, walls = mazegen(size)
position = '{}'.format(grid[size*2][size])
while True:
    if flag == False or dir == 'quit':
        print('Thanks for playing!')
        break
    if position == 'win':
        print('You did it!')
        break
    print_grid(grid, position, walls, int(mode), size)
    dir = input('#')
    position = move(position, dirs, dir, grid, walls)
