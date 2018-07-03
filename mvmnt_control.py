from symbols import symbls

symbols, rows, columns = symbls()

def move(pos, dirs, dir, grid, walls):
	splt_pos = [char for char in pos]
	if dir in dirs.values():
		if dir == dirs['up'] and grid[symbols.index(splt_pos[0])*2+1][symbols.index(splt_pos[1])+1] != '--':
			if pos == '00':
				return 'win'
			else:
				splt_pos[0] = symbols[symbols.index(splt_pos[0])-1]
		elif dir == dirs['down'] and grid[symbols.index(splt_pos[0])*2+3][symbols.index(splt_pos[1])+1] != '--':
			splt_pos[0] = symbols[symbols.index(splt_pos[0])+1]
		elif dir == dirs['left'] and symbols.index(splt_pos[1]) > 0 and walls[symbols.index(splt_pos[0])][symbols.index(splt_pos[1])-1] != 1:
			splt_pos[1] = symbols[symbols.index(splt_pos[1])-1]
		elif dir == dirs['right'] and symbols.index(splt_pos[1]) < len(walls)-1 and walls[symbols.index(splt_pos[0])][symbols.index(splt_pos[1])] != 1:
			splt_pos[1] = symbols[symbols.index(splt_pos[1])+1]
	pos = str(splt_pos[0] + splt_pos[1])
	return pos
