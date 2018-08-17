from mazegen import *
from mvmnt_control import move
from ui import *
# from sys import argv
# #MODE '0' - WITHOUT GRID ENNUMERATION VISIBLE
# #MODE '1' (OR ANYTHING ELSE THAN 0 ACTUALLY) - WITH GRID ENNUMERATION VISIBLE
# try:
#     script, mode = argv
# except:
#     mode = 1

#DEFAULT VALUES
dirs = {
    'up': 'u',
    'down': 'd',
    'left': 'l',
    'right': 'r'
}
size = 5

flag, size, dirs = getmenu(size, dirs)

if flag != False:
    grid = mazegen(size)
    start_cell = grid[size**2 - 1]
    position = start_cell.row + start_cell.col

while True:
    if flag == False or dir == 'quit':
        print('Thanks for playing!')
        break
    if position == 'win':
        print('You did it!')
        break
    print_grid(grid, position)
    dir = input('#')
    position = move(position, dirs, dir, grid)
