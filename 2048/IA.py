import os
import random
import time
import keyboard

import motor
tamanoCuadricula = 4

class Exception (Exception):
	pass

def move (direction, inputGrid, screen = True, newRandom = True):
	previousValues = motor.getValues (inputGrid.copy ())

	if direction == "left":
		inputGrid = controller.moveLeft (inputGrid)
	elif direction == "up":
		inputGrid = controller.moveUp (inputGrid)
	elif direction == "right":
		inputGrid = controller.moveRight (inputGrid)
	elif direction == "down":
		inputGrid = controller.moveDown (inputGrid)
	else:
		raise Exception ("Invalid direction")

	random = not motor.compare (previousValues, motor.getValues (inputGrid.copy ()))
	if random and newRandom:
		inputGrid = controller.newRandom (inputGrid.copy ())
	if screen:
		motor.display (inputGrid)
		pass
	return inputGrid, random


left = True
right = True
up = True
down = True
grid = motor.start (tamanoCuadricula)
controller = motor.Gestor ()

def emptySpaces (inputGrid):
	directions = ['right', 'up', 'down', 'left']
	apt = []
	options = []
	values = []
	empty = []
	for i in directions:
		returned = move (i, inputGrid, screen = False)
		options.append (returned [0])
		apt.append (returned [1])
	for i in options:
		values.append (motor.getValues (i))
	for i in values:
		for x in range (tamanoCuadricula):
			empty.append (0)
			for y in range (tamanoCuadricula):
				if i [x][y] == 0:
					empty[x] += 1
	empty = empty [:tamanoCuadricula]

	maximum = max (empty)
	return empty.index (maximum)

def priority (inputGrid):
	directions = ['left', 'down', 'up', 'right']
	for i in directions:
		waste, result = move (i, inputGrid, screen = False)
		if result:
			return i

def bestTry(inputGrid):
	pass

while True:
	dirs = priority (grid)

	try:
		grid, waste = move (dirs, grid)
		#print (directions [empty.index (max)])
	except:
		motor.display (grid)
		print ("Has perdido")
		values = motor.getValues (grid)
		maxList = []
		for i in values:
			maxList.append (max (i))
		print (f"El mejor bloque es {max (maxList)}")

		#time.sleep (0.5)
		grid = motor.start (tamanoCuadricula)
	values = motor.getValues (grid)
	for x in range (tamanoCuadricula):
		for y in range (tamanoCuadricula):
			if values [x][y] == 2048:
				motor.display (grid)
				print ("Has ganado")
				while True:
					pass
	time.sleep (0)