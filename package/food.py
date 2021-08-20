from random import randint

import pygame
from .vector import Vector
from .constants import width, height, size

class Food(Vector):
	color = (171,219,227)
	def __init__(self):
		super().__init__(randint(0, width - size), randint(0, height - size))

	def draw(self, win):
		pygame.draw.rect(win, self.color, pygame.Rect(self.x - size / 2, self.y - size / 2, size, size))