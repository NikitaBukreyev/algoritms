from random import randint
from enum import Enum

class MAP_ENTRY_TYPE(Enum): # это перечисление определяет различные типы ячеек, которые могут присутствовать на карте.
	MAP_EMPTY = 0,
	MAP_BLOCK = 1,
	MAP_TARGET = 2,
	MAP_PATH = 3,

class WALL_DIRECTION(Enum):  # это перечисление определяет различные направления, в которых может быть обращена стена.
	WALL_LEFT = 0,
	WALL_UP = 1,
	WALL_RIGHT = 2,
	WALL_DOWN = 3,
	
map_entry_types = {0:MAP_ENTRY_TYPE.MAP_EMPTY, 1:MAP_ENTRY_TYPE.MAP_BLOCK, 2:MAP_ENTRY_TYPE.MAP_TARGET, 3:MAP_ENTRY_TYPE.MAP_PATH}
# сопоставляет целочисленные значения с элементами перечисления MAP_ENTRY_TYPE. 
# Это используется методом getType для преобразования целочисленного значения ячейки в соответствующее значение MAP_ENTRY_TYPE.
class Map():
	def __init__(self, width, height):                                         
		self.width = width
		self.height = height
		self.map = [[0 for x in range(self.width)] for y in range(self.height)]
# конструктор класса Map, который инициализирует ширину и высоту карты и создает пустую двумерную сетку ячеек с указанными размерами.	
	def generatePos(self, rangeX, rangeY):
		x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
		while self.map[y][x] == 1:
			x, y = (randint(rangeX[0], rangeX[1]), randint(rangeY[0], rangeY[1]))
		return (x , y)
# этот метод генерирует случайную позицию (x, y) в пределах указанного диапазона значений x и y. 
# Он продолжает генерировать новые случайные позиции, пока не найдет ту, которая не является заблокированной ячейкой (т. е. ячейкой со значением 1).	
	def resetMap(self, value):
		for y in range(self.height):
			for x in range(self.width):
				self.setMap(x, y, value)
# этот метод сбрасывает всю карту, устанавливая для всех ячеек указанное значение.
	def setMap(self, x, y, value):
		if value == MAP_ENTRY_TYPE.MAP_EMPTY:
			self.map[y][x] = 0
		elif value == MAP_ENTRY_TYPE.MAP_BLOCK:
			self.map[y][x] = 1
		elif value == MAP_ENTRY_TYPE.MAP_TARGET:
			self.map[y][x] = 2
		else:
			self.map[y][x] = 3
# этот метод устанавливает значение ячейки в позиции (x, y) на указанное значение.
	def isVisited(self, x, y):
		return self.map[y][x] != 1
# этот метод возвращает True, если ячейка в позиции (x, y) не была посещена (т. е. ее значение не равно 1), и False в противном случае.
	def isMovable(self, x, y):
		return self.map[y][x] != 1
# этот метод возвращает True, если ячейка в позиции (x, y) не является заблокированной ячейкой (т. е. ее значение не равно 1), и False в противном случае.	
# 	
	def isValid(self, x, y):
		if x < 0 or x >= self.width or y < 0 or y >= self.height:
			return False
		return True
# этот метод возвращает True, если позиция (x, y) находится в пределах границ карты, и False в противном случае.	
	def getType(self, x, y):
		return map_entry_types[self.map[y][x]]
# этот метод возвращает тип ячейки в позиции (x, y) как элемент перечисления MAP_ENTRY_TYPE.
	def showMap(self):
		for row in self.map:
			s = ''
			for entry in row:
				if entry == 0:
					s += ' 0'
				elif entry == 1:
					s += ' #'
				else:
					s += ' X'
			print(s)
# этот метод выводит карту на консоль с заблокированными ячейками, представленными '#', и всеми остальными ячейками, представленными символом пробела.	