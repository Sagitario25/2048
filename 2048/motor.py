import random
import os

def invertY (inputGrid):
	gridSize = getGridSize (inputGrid)
	outputGrid = []
	for x in range (0, gridSize):
		outputGrid.append ([])
		for y in range (0, gridSize):
			outputGrid [x].append (Cuadro (x, y, inputGrid [x][gridSize - y - 1].value))
	return outputGrid
def invertX (inputGrid):
	gridSize = getGridSize (inputGrid)
	outputGrid = []
	for x in range (0, gridSize):
		outputGrid.append ([])
		for y in range (0, gridSize):
			outputGrid [x].append (Cuadro (x, y))

	for x in range (0, gridSize):
		for y in range (0, gridSize):
			outputGrid [x][y].value = inputGrid [gridSize - x - 1][y].value
	return outputGrid

def getGridSize (inputGrid):
	return len (inputGrid)

def newAviableGrid (inputGrid):
	gridSize = getGridSize (inputGrid)
	aviableGrid = []
	for x in range (0, gridSize):
		aviableGrid.append ([])
		for y in range (0, gridSize):
			aviableGrid [x].append (True)
	return aviableGrid

class Gestor:
	def __init__ (self):
		pass

	def newRandom (self, inputGrid):
		gridSize = getGridSize (inputGrid)
		self.grid = inputGrid
		self.empty = []
		for x in range (gridSize):
			for y in range (gridSize):
				if self.grid [x][y].value == 0:
					self.empty.append ((x, y))
		self.random = random.randint (1, len (self.empty)) - 1
		if random.random () < 0.75:
			self.newValue = 2
		else:
			self.newValue = 4
		self.grid [self.empty [self.random][0]][self.empty [self.random][1]].value = self.newValue
		return self.grid


	def moveLeft (self, inputGrid):
		gridSize = getGridSize (inputGrid)
		self.grid = inputGrid
		self.aviableGrid = newAviableGrid (self.grid)
		for y in range (0, gridSize):
			for x in range (0, gridSize):
				if self.grid [x][y].value != 0:
					self.grid, self.aviableGrid = self.grid[x][y].moveLeft(self.grid, self.aviableGrid)
		return self.grid

	def moveRight (self, inputGrid):
		self.grid = invertX (inputGrid)
		self.grid = self.moveLeft (self.grid)
		self.grid = invertX (self.grid)
		return self.grid

	def moveUp (self, inputGrid):
		gridSize = getGridSize (inputGrid)
		self.grid = inputGrid
		self.aviableGrid = newAviableGrid (self.grid)
		for x in range (0, gridSize):
			for y in range (0, gridSize):
				if self.grid [x][y].value != 0:
					self.grid, self.aviableGrid = self.grid[x][y].moveUp(self.grid, self.aviableGrid)
		return self.grid

	def moveDown (self, inputGrid):
		self.grid = invertY (inputGrid)
		self.grid = self.moveUp (self.grid)
		self.grid = invertY (self.grid)
		return self.grid

class Cuadro:
	def __init__ (self, x, y, value = 0):
		self.x = x
		self.y = y
		self.value = value

	def moveLeft (self, inputGrid, aviableGrid):
		self.grid = inputGrid
		self.aviableGrid = aviableGrid
		if self.aviableGrid == None:
			self.aviableGrid = newAviableGrid (self.grid)

		#Get moving point
		self.counter = self.x - 1
		while True:
			if self.counter < 0:
				break
			if self.grid [self.counter][self.y].value == 0:
				self.counter -= 1
			elif self.grid [self.counter][self.y].value != self.grid [self.x][self.y].value:
				self.counter += 1
				break
			if not self.aviableGrid [self.counter][self.y]:
				self.counter += 1
				break
			if self.grid [self.counter][self.y].value == self.grid [self.x][self.y].value:
				break
		if self.counter < 0:
			self.counter = 0
		#Change values
		if self.counter != self.x:
			if self.grid [self.counter][self.y].value != 0:
				self.aviableGrid [self.counter][self.y] = False
			self.grid [self.counter][self.y].value +=  self.grid [self.x][self.y].value
			self.grid [self.x][self.y].value = 0
		return self.grid, self.aviableGrid

	def moveUp (self, inputGrid, aviableGrid):
		self.grid = inputGrid
		self.aviableGrid = aviableGrid
		if self.aviableGrid == None:
			self.aviableGrid = newAviableGrid (self.grid)

		#Get moving point
		self.counter = self.y - 1
		while True:
			if self.counter < 0:
				break
			if self.grid [self.x][self.counter].value == 0:
				self.counter -= 1
			elif self.grid [self.x][self.counter].value != self.grid [self.x][self.y].value:
				self.counter += 1
				break
			if not self.aviableGrid [self.x][self.counter]:
				self.counter += 1
				break
			if self.grid [self.x][self.counter].value == self.grid [self.x][self.y].value:
				break
		if self.counter < 0:
			self.counter = 0
		#Change values
		if self.counter != self.y:
			if self.grid [self.x][self.counter].value != 0:
				self.aviableGrid [self.x][self.counter] = False
			self.grid [self.x][self.counter].value +=  self.grid [self.x][self.y].value
			self.grid [self.x][self.y].value = 0
		return self.grid, self.aviableGrid


def display (inputGrid):
	gridSize = getGridSize (inputGrid)
	#os.system ('cls')
	values = []
	for x in range (0, gridSize):
		values.append ([])
		for y in range (0, gridSize):
			if str (inputGrid[y][x].value) == '0':
				values [x].append (' ')
			else:
				values [x].append (str (inputGrid[y][x].value))
	for a in values:
		message = "|"
		for b in a:
			#Agregar espacios
			temp = b
			for c in range (0, 4 - len (b)):
				temp += ' '
			message += temp + '|'
		bars = ""
		for i in range (0, len (message)):
			bars += '_'
		print (bars)
		print (message)

	print (bars)

def getValues (grid):
	gridSize = getGridSize (grid)
	values = []
	for x in range (0, gridSize):
		values.append ([])
		for y in range (0, gridSize):
			values [x].append (grid [x][y].value)
	return values

def compare (grid1, grid2):
	gridSize = getGridSize (grid1)
	values1 = grid1
	values2 = grid2
	same = True
	for x in range (0, gridSize):
		for y in range (0, gridSize):
			if values1 [x][y] != values2 [x][y]:
				same = False
	return same

def start (size):
	gridSize = size
	startingGrid = []
	for x in range (0, gridSize):
		startingGrid.append ([])
		for y in range (0, gridSize):
			startingGrid [x].append (Cuadro (x, y))
	controller = Gestor ()
	startingGrid = controller.newRandom (startingGrid)
	startingGrid = controller.newRandom (startingGrid)
	display (startingGrid)
	return startingGrid