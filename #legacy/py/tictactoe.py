def tictactoe():
	matrix = {1: '#', 2: '#', 3: '#', 4: '#', 5: '#', 6: '#', 7: '#', 8: '#', 9: '#'}
	turn = 0
	while 1:
		while 1:
			print('\n' * 50, matrix[1], '│', matrix[2], '│', matrix[3], '\n', '─', '┼', '─', '┼', '─', '\n', matrix[4], '│', matrix[5], '│', matrix[6], '\n', '─', '┼', '─', '┼', '─', '\n', matrix[7], '│', matrix[8], '│', matrix[9], '\n')
			loc = input(' ▲ PLAY TABLE\n ▼ EXAMPLE POSITIONS\n\n 1│2│3\n ─┼─┼─\n 4│5│6\n ─┼─┼─\n 7│8│9\n\n Introdueixi el pròxim moviment: ')
			if not loc.isdigit():
				break
			elif 0 < int(loc) < 10:
				loc = int(loc)
			else:
				break
			if (loc == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9) and matrix[loc] == '#':
				if turn == 0:
					matrix[loc] = 'X'
					turn = 1
				else:
					matrix[loc] = '0'
					turn = 0


tictactoe()
