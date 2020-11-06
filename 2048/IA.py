import os
import random
import time
import keyboard

import motor
tamanoCuadricula = 4


def move (direction, inputGrid, screen = True):
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
		print ("Eso no es una dirrecion correcta")

	random = not motor.compare (previousValues, motor.getValues (inputGrid.copy ()))
	if random:
		inputGrid = controller.newRandom (inputGrid.copy ())
	if screen:
		#display (inputGrid)
		pass
	return inputGrid, random


left = True
right = True
up = True
down = True
grid = motor.start (tamanoCuadricula)
controller = motor.Gestor ()

while True:
	directions = ['left', 'right', 'up', 'down']
	apt = []
	options = []
	values = []
	empty = []
	for i in directions:
		returned = move (i, grid, False)
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

	maximum = -1
	for i in range (len (empty)):
		if empty [i] > maximum and apt[i]:
			maximum = empty [i]

	try:
		grid, waste = move (directions [empty.index (maximum)], grid)
		#print (directions [empty.index (max)])
	except:
		motor.display (grid)
		print ("Has perdido")
		values = motor.getValues (grid)
		maxList = []
		for i in values:
			maxList.append (max (i))
		print (f"El mejor bloque es {max (maxList)}")

		time.sleep (0.5)
		grid = motor.start (tamanoCuadricula)
	values = motor.getValues (grid)
	for x in range (tamanoCuadricula):
		for y in range (tamanoCuadricula):
			if values [x][y] == 2048:
				display (grid)
				print ("Has ganado")
				while True:
					pass
	time.sleep (0)