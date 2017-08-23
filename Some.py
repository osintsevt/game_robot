#Подключаем библиотеку времени
from time import sleep as timeout

#Основной класс
class Robot():
	#Инициализация робота
	def __init__(self, name, hp, power, defen):
		self.name      = name
		self.hp        = hp
		self.power     = power
		self.defen     = defen
		self.max_hp    = self.hp
		self.max_defen = self.hp
		print('\nРобот '+ self.name +' создан и готов к битве\n===================================================\n')

	#Лечение
	def heal(self,live,status = 'normal'):
		if self.hp + 2 < self.max_hp or status == 'cheet':
			self.hp     = self.hp + live
			print('Робот ' + self.name + ' восстановил ' + str(live) + ' HP!')
		else:
			self.hp =  self.max_hp
			print('Робот ' + self.name + ' полностью восстановленю')

	#Защита
	def protect(self,guard,status = 'normal'):
		if self.defen + 0.5 < self.max_defen or status == 'cheet':
			self.defen  = self.defen + guard
			print('Робот ' + self.name + ' встал в защитную стойку.')
		else:
			self.defen = self.max_defen
			print('Защита робота ' + self.name + ' максимальна.')

	#Атака
	def attack(self, opponent):
		opponent.hp = round (opponent.hp - self.power + opponent.defen / 5, 1)
		if opponent.hp > 0:
			print('Робот ' + self.name + ' бьется против ' + opponent.name + '!\nУ ' + opponent.name + ' осталось всего ' + str(opponent.hp )+ 'HP!' )
		else:
			print('Робот ' + self.name + ' бьется против ' + opponent.name + '!\nУ ' + opponent.name + ' не осталось HP!')

	#Удаление робота
	def __del__(self):
		global a
		if a == 0:
			print('Робот '+ self.name + ' проиграл и разбился на части, сожалею...')

#Функции
#Создание робота по конфигурации и имени
def verify_conf(param, name):
	if (param == 'a') or (param == 'а'):
		bot = Robot(name = name, hp = 20, power = 1.5, defen = 0.5)
	elif (param == 'b') or (param == 'б'):
		bot = Robot(name = name, hp = 15, power = 2.5, defen = 0.5)
	elif (param == 'c') or (param == 'в'):
		bot = Robot(name = name, hp = 15, power = 1.5, defen = 1.0)
	else:
		error(0)
	return bot

#Получение имени робота от пользователя
def set_name(num):
	if (num == 1) or (num == 2):
		name = input('Игрок ' + str(num) + ', введите имя своего робота\n>')
	else:
		error(2)
	return name

#Получение конфигурации робота от пользователя
def set_conf(num):
	if (num == 1):
		global name_1
		conf = input('Игрок ' + str(num) + ', выберите конфигурацию вашего робота ' + name_1 + ':\na) Стандарт\nб) Бой-машина\nв) Танк\n\n>')
	elif (num == 2):
		global name_2
		conf = input('Игрок ' + str(num) + ', выберите конфигурацию вашего робота ' + name_2 + ':\na) Стандарт\nб) Бой-машина\nв) Танк\n\n>')
	else:
		error(3)
	return conf

#Выбрасывание ошибки
def error(param):
	print('Ошибка ' + str(param))
	timeout(1)
	exit()

#Выбор действия пользователя
def select(owner):

	global robot_1
	global robot_2

	name = robot_1.name if owner == 1 else robot_2.name
	hp   = robot_1.hp if owner == 1 else robot_2.hp

	print('Игрок ' + str(owner) + ', что будет делать ваш робот?\n\n' + name + ' (' + str(hp) +' HP) :\n |\n |\_a) Биться\n |\_б) Лечиться\n  \_в) Защищаться\n')
	
	result = input('>')
	return result

#Главная функция хода
def turn(owner):

	global robot_1
	global robot_2

	selection = 'x'

	obj = robot_1 if owner ==  1 else robot_2
	opp = robot_2 if obj == robot_1 else robot_1

	while selection not in ['a','b','c','а','б','в','cheet']:
		selection = select(owner)
	if selection in ['a','а']:
		obj.attack(opponent = opp)
	elif selection in ['b', 'б']:
		obj.heal(live = 1)
	elif selection in ['cheet']:
		obj.heal(live = 1000, status = 'cheet')
		obj.protect(guard = 1000, status = 'cheet')
		obj.power = 1000
		obj.attack(opponent = opp)
	else:
		obj.protect(guard = 0.5)

a = 0

#Первый робот
name_1 = set_name(1)
robot_1 = verify_conf(param = set_conf(1), name = name_1)

#Второй робот
name_2 = set_name(2)
robot_2 = verify_conf(param = set_conf(2), name = name_2)

#Оснвной цикл
while (robot_1.hp > 0 ) and (robot_2.hp > 0):
	turn(1)
	if (robot_1.hp <= 0) or (robot_2.hp <= 0):
		break
	turn(2)

#Конец игры
winner = robot_1 if robot_2.hp <= 0 else robot_2
looser = robot_2 if winner == robot_1 else robot_1
looser.__del__()
print('Поздравляю! Робот ' + winner.name + ' победил!\nНажмите ENTER чтобы закончить')
a = input('')