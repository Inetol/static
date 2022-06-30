import os, random, time


# Classe "Memory", serveix per poder crear i modificar variables dinàmicament i fàcilment entre classes.
class Memory:
	# Escriu a una variable a una ID, després retorna el contingut.
	def write(self, _data, _value): globals()[_data] = _value

	# Llegeix a una variable a una ID, després retorna el contingut.
	def read(self, _data): return globals()[_data]


# Classe "Menu", conte la base del programa.
class Menu:
	# Neteja el contingut en pantalla.
	def clear(self):
		return os.system('cls' if os.name in ('nt', 'dos') else 'clear')

	# Comprova que "n" estigui entre "_min" i "_max", retorna una "Bool".
	def check(self, _min, _max, n):
		if not n.isdigit(): return False
		elif _min <= int(n) <= _max: return True
		else: return False

	# Funció que redirigeix a una selecció del menú mitjançant "_n".
	def option(self, _n):
		# Selecció #1
		def one():
			if memory.read('dynamic_list')[memory.read('player')] == memory.read('priv_list'):
				menu.clear()
				print('Ha gunyat el jugador ' + str(memory.read('player')) + '!')
				memory.write('ingame', False)
			else:
				menu.clear()
				print('Incorrecte.')
				time.sleep(1)

		# Selecció #2
		def two():
			while True:
				menu.clear()
				print(str(memory.read('dynamic_list')[memory.read('player')]) + '\n')
				origin = input('Introdueixi la posició d\'origen. Entre 0 i ' + str(len(memory.read('dynamic_list')[memory.read('player')]) - 1) + ": ")
				destination = input('Introdueixi la posició de desti. Entre 0 i ' + str(len(memory.read('dynamic_list')[memory.read('player')]) - 1) + ": ")
				if not menu.check(0, len(memory.read('dynamic_list')[memory.read('player')]) - 1, origin) or not menu.check(0, len(memory.read('dynamic_list')[memory.read('player')]) - 1, destination): continue
				matrix = memory.read('dynamic_list')
				loc1 = memory.read('dynamic_list')[memory.read('player')][int(origin)]
				loc2 = memory.read('dynamic_list')[memory.read('player')][int(destination)]
				matrix[memory.read('player')][int(origin)] = loc2
				matrix[memory.read('player')][int(destination)] = loc1
				menu.clear()
				memory.write('dynamic_list', matrix)
				print('Has modificat l\'ordre:\n\n' + str(matrix[memory.read('player')]))
				memory.write('player', 1) if memory.read('player') == 0 else memory.write('player', 0)
				time.sleep(3)
				break

		# Selecció #3
		def three():
			matrix = memory.read('dynamic_list')
			matrix[memory.read('player')] = memory.read('static_list')
			memory.write('dynamic_list', matrix)
			menu.clear()
			print('Fet.')
			time.sleep(1)

		if _n == 1: one()
		elif _n == 2: two()
		elif _n == 3: three()

	# Ensenya l'estat actual de la paraula amb el menú de selecció.
	def run(self):
		while memory.read('ingame'):
			menu.clear()
			print('Tenim aquesta paraula: "' + ''.join(memory.read('dynamic_list')[memory.read('player')]) + '"\n\nQue desitges fer jugador ' + str(memory.read('player') + 1) + '?')
			print("#1 | Verificar paraula\n#2 | Moure posició lletra\n#3 | Reinicia l'ordre de la paraula")
			option = input('\nIntrodueix un numero: #')
			if menu.check(0, 3, option): menu.option(int(option))


# Inicia les classes.
menu = Menu()
memory = Memory()

# Estableix les variables inicials.
memory.write('ingame', True)
memory.write('player', 0)
memory.write('priv_list', list(open('src/ktw/w_list.txt').readlines()[random.randrange(0, len(open('src/ktw/w_list.txt').readlines()))].replace('\n', '').strip(' ')))
memory.write('static_list', memory.read('priv_list').copy())
random.shuffle(memory.read('static_list'))
memory.write('dynamic_list', [])
memory.read('dynamic_list').append(memory.read('static_list').copy())
memory.read('dynamic_list').append(memory.read('static_list').copy())

menu.clear()
menu.run()
