public, private = [], []


def cc():
	print('\n' * 50)


def check(s):
	pos, found = 0, 0
	if s == '': return
	for _w in private:
		if s in _w:
			found = 1
			public[pos] = s
		pos += 1
	return found


def draw(n):
	if n == 0:
		print('')
	elif n == 1:
		print(' |\n|\n|\n|\n')
	elif n == 2:
		print(' |-----\n |\n |\n |\n')
	elif n == 3:
		print(' |-----\n |    O\n |\n |\n')
	elif n == 4:
		print(' |-----\n |    O\n |    |\n |\n')
	elif n == 5:
		print(' |-----\n |    O\n |   /|\n |\n')
	elif n == 6:
		print(' |-----\n |    O\n |   /|\\ \n |\n')
	elif n == 7:
		print(' |-----\n |    O\n |   /|\\ \n |   /\n')
	elif n == 8:
		print(' |-----\n |    O\n |   /|\\ \n |   / \\ \n')


def hangged():
	counter = 0
	cc()
	word = input('Introdueixi la paraula que vol mostrar: ')
	for s in word:
		private.append(s)
		public.append('_')
	while counter <= 9:
		if counter == 8:
			cc()
			print('Has perdut! La paraula era: ' + word + '\n')
			draw(8)
			break
		cc()
		draw(counter)
		print(' '.join(draw(str, public)))
		letter = input('Introdueixi alguna lletra: ')
		if check(letter) == 0: counter += 1


hangged()
