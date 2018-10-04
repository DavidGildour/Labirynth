def getmenu(size, dirs, optn = '0'):
    if optn == '0':
        print("""
        Welcome to Labirynth - a game of mazes!

        MENU:
        1. Start game
        2. Options
        3. About
        4. Exit

        """)
    while optn != '4':
        if not optn.isdigit() or int(optn) > 4:
            optn = input('#')
            continue
        optn = input('#')
        if optn == '1':
            return True, size, dirs
        if optn == '2':
            return menu_options(size, dirs)
        if optn == '3':
            return menu_about(size, dirs)
    return False, size, dirs

def menu_options(size, dirs, optn = '0'):
    if optn == '0':
        print("""
        OPTIONS:
        1. Set controls
        2. Set size
        3. Back
        """)
    while optn != '3':
        if not optn.isdigit() or int(optn) > 3:
            optn = input('#')
            continue
        optn = input('#')
        if optn == '1':
            return options_controls(size, dirs)
        if optn == '2':
            return options_size(size, dirs)
    return getmenu(size, dirs)

def menu_about(size, dirs):
    with open('README.md') as f:
        print(f.read())
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
    size = input('Set the size of the maze (3-34): ')
    while not size.isdigit() or (int(size) < 3 or int(size) > 34):
        print("Wrong input.")
        size = input('Set the size of the maze (3-34): ')
    return menu_options(int(size), dirs)
