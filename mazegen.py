"""TO DO:
ENHANCE MAZE GENERATING ALGORITHMS"""

import random
from symbols import symbls

symbols, rows, columns = symbls()

def getmenu(size, dirs, optn = 0):
    if optn == 0:
        print("""
        Welcome to Labirynth - a game of mazes!

        MENU:
        1. Start game
        2. Options
        3. About
        4. Exit

        """)
    while optn != 4:
        optn = int(input('#'))
        if optn == 1:
            return True, size, dirs
        if optn == 2:
            return menu_options(size, dirs)
        if optn == 3:
            return menu_about(size, dirs)
    return False, size, dirs

def menu_options(size, dirs, optn = 0):
    if optn == 0:
        print("""
        OPTIONS:
        1. Set controls
        2. Set size
        3. Back
        """)
    while optn != 3:
        optn = int(input('#'))
        if optn == 1:
            return options_controls(size, dirs)
        if optn == 2:
            return options_size(size, dirs)
    return getmenu(size, dirs)

def menu_about(size, dirs):
    print(open('about.txt').read())
    input()
    return getmenu(size, dirs)

def options_controls(size, dirs):
    print("SET CONTROLS:")
    dirs['up'] = input('Press button for "up": ')
    dirs['down'] = input('Press button for "down": ')
    dirs['left'] = input('Press button for "left": ')
    dirs['right'] = input('Press button for "right": ')
    return menu_options(size, dirs)

def options_size(size, dirs):
    size = int(input('Set the size of the maze (from 3 up to 34 but for comfortable vision you shouldnt exceed 14): '))
    return menu_options(size, dirs)

def print_grid(grid, pos, ver_walls, md, size):
    """THIS IS ONLY FOR PRINTING THE GRID.
    DON'T MESS WITH THE GRID WITHIN THIS FUNCTION.
    """
    splt_pos = [char for char in pos]
    #THIS REPLACES THE GIVEN CELL IN THE GRID (POS ARGUMENT) WITH '##'
    grid[int(rows.index(splt_pos[0]))*2+2][columns.index(splt_pos[1]) + 1] = '##'
    for row in grid:
        for elem in row:
            if '--' in row:
                print(elem, end = ' + ')
            elif row == grid[0]:
                print(elem, end = '   ')
            #ATTENTION! CONSTRUCTING VERTICAL WALLS BASED ON
            #A ver_walls MATRIX IS HAPPENING HERE!
            elif elem[0] in symbols and elem[1] in symbols and grid.index(row) > 1 and row.index(elem) > 0:
                if ver_walls[int(grid.index(row)/2) - 1][row.index(elem) - 1] == 0 and row.index(elem) != 0 and row.index(elem) != size:
                    if md == 0:
                        print('  ', end = '   ')
                    else:
                        print(elem, end = '   ')
                else:
                    if md == 0:
                        print('  ', end = ' | ')
                    else:
                        print(elem, end = ' | ')
            elif elem == '##' and splt_pos != ['{}'.format(size - 1) for i in range(2)] and ver_walls[int(grid.index(row)/2) - 1][row.index(elem) - 1] == 0:
                print(elem, end = '   ')
            else:
                print(elem, end = ' | ')
        print('\n')
    #THIS REVERSES THE REPLACEMENT AT THE BEGINNING OF THE FUNCTION, THUS
    #ALLOWING TO REPLACE IT ONCE AGAIN WITHOUT LEAVING A TRACE
    grid[rows.index(splt_pos[0])*2+2][columns.index(splt_pos[1])+1] = '{}{}'.format(splt_pos[0], splt_pos[1])

def mazegen(size):
    grid = []
    #THIS INSERTS AN EMPTY ROW AT THE TOP (WHICH CAUSES THE NEXT ROW TO BE OUTLINED)
    grid.insert(0, ['  ' for i in range(size)])
    #THIS GENERATES THE ENTIRE GRID
    for j in range(size*2):
        if j % 2 == 0:
            grid.append(['--' for k in range(size)])
        else:
            grid.append(['{}{}'.format(rows[j//2],columns[i]) for i in range(size)])
    #THIS INSERTS THE LINING ON THE BOTTOM
    grid.append(['--' for i in range(size)])
	#PLACING ENTRANCE AND EXIT
    grid[1][0] = '  '
    grid[len(grid)-1][size-1] = '  '
    #ATTENTION! CONSTRUCTING RANDOM HORIZONTAL WALLS HERE!
    for wall_row in range(len(grid)):
        if wall_row % 2 == 0:
            continue
        if wall_row > 1 and wall_row != len(grid) - 1:
            for i in range(random.randint(1, size - 2)):
                grid[wall_row][random.randrange(0, size)] = '  '
    #ATTENTION! DETERMINING WHERE TO PUT THE VERTICAL WALLS
    ver_walls = []
    for row in grid:
        #THIS ALGORITHM IS TAKING THE ROWS WITH ACTUAL CELLS
        if grid.index(row) in [x*2 for x in range(1, size+1)]:
            #CONSTRUCTS RANDOM ver_walls MATRIX ROW FOR VERTICAL WALL-CONSTRUCTING IN CURRENT ROW
            ver_walls.append([random.randint(0, 1) for i in range(size)])
            ##THIS LINE IS FOR DIAGNOSTICS
            #print(int(grid.index(row)/2)-1, ver_walls[int(grid.index(row)/2)-1])
            #THIS MAKES SURE ALL THE ROWS HAVE AN ENTRANCE AND AN EXIT NOT INACCESIBLE
            lft = 99
            rght = 99
            for i in range(size):
                if lft == 99 and (grid[grid.index(row)-1][i] == '  ' or grid[grid.index(row)+1][i] == '  '):
                    lft = i
                    continue
                if grid[grid.index(row)-1][i] == '  ' or grid[grid.index(row)+1][i] == '  ':
                    rght = i+1
                if lft != 99 and rght != 99 and rght-lft == 0:
                    ver_walls[int(grid.index(row)/2)-1][lft] = 0
                elif lft != 99 and rght != 99 and ver_walls[int(grid.index(row)/2)-1][lft:rght] != [0 for i in range(rght-lft)]:
                    ver_walls[int(grid.index(row)/2)-1][lft:rght] = [0 for i in range(rght-lft)]
                    lft = 99
                    rght = 99
            ##THIS LINE IS FOR DIAGNOSTICS
            #print(int(grid.index(row)/2)-1, ver_walls[int(grid.index(row)/2)-1])
            #CHECKS FOR LACK OF CORRIDORS AND RANDOMLY ADDS WHERE NEEDED
            if grid.index(row) > 2:
                for i in range (size-1):
                    if ver_walls[int(grid.index(row)/2)-2][i] == 0 and ver_walls[int(grid.index(row)/2-1)][i] == 0 and grid[grid.index(row)-1][i] == '  ' and grid[grid.index(row)-1][i+1] == '  ':
                        t = random.randrange(0, 4)
                        if t == 0:
                            ver_walls[int(grid.index(row)/2)-2][i] = 1
                        elif t == 1:
                            ver_walls[int(grid.index(row)/2-1)][i] = 1
                        elif t == 2:
                            grid[grid.index(row)-1][i+1] = '--'
                        elif t == 3:
                            grid[grid.index(row)-1][i] = '--'
    #OUTLINING THE LEFT SIDE OF THE GRID
    for row in grid:
        row.insert(0, ' ')

    ##THIS LINE IS FOR DIAGNOSTICS
    #print('\n')
    #for row in ver_walls:
    #    print(row)
    return grid, ver_walls
