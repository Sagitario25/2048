import os
import random
import time
import keyboard

import motor
tamanoCuadricula = 4

grid = motor.start (tamanoCuadricula)

def move (direction, inputGrid):
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

	if not motor.compare (previousValues, motor.getValues (inputGrid.copy ())):
		inputGrid = controller.newRandom (inputGrid.copy ())
	motor.display (inputGrid)
	return inputGrid


left = True
right = True
up = True
down = True

controller = motor.Gestor ()

while True:
	if keyboard.is_pressed ('esc'):
		exit ()
	if keyboard.is_pressed ('left'):
		if left:
			left = False
			grid = move ('left', grid)
	else:
		left = True

	if keyboard.is_pressed ('right'):
		if right:
			right = False
			grid = move ('right', grid)
	else:
		right = True

	if keyboard.is_pressed ('up'):
		if up:
			up = False
			grid = move ('up', grid)
	else:
		up = True

	if keyboard.is_pressed ('down'):
		if down:
			down = False
			grid = move ('down', grid)
	else:
		down = True 