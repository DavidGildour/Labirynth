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


def setup():
    grid = mazegen(size)
    start_cell = grid[size**2 - 1]
    position = start_cell.row + start_cell.col
    steps = 0
    return grid, start_cell, position, steps

def main():
    flag, size, dirs = getmenu(size, dirs)
    if flag != False:
        grid, start_cell, position, steps = setup()

    while True:
        if flag == False or dir == 'quit':
            print('Thanks for playing!')
            break
        elif position == 'win':
            print('You did it! And only in {} steps! Wow!'.format(steps))
            decision = input('Want to continue? (y/n) ')
            if decision == 'y':
                size += 1
                grid, start_cell, position, steps = setup()
                continue
            else:
                flag = False
                continue
        print_grid(grid, position)
        dir = input('#')
        if position != move(position, dirs, dir, grid):
            steps += 1
        position = move(position, dirs, dir, grid)

if __name__ == '__main__':
    main()
