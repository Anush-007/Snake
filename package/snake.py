import pygame
from .constants import width, height, size
from .vector import Vector
from enum import Enum
from random import choice

class Direction(Enum):
	left = Vector(-1, 0)
	right = Vector(1, 0)
	up = Vector(0, -1)
	down = Vector(0, 1)



class Snake():
	color = (233, 90, 114)
	def __init__(self, start, speed = 10, body = []) -> None:
		self.snake = []
		self.snake.append(Vector(*start))
		self.speed = speed
		self.veldir = choice(list(Direction))
		self.size = size
		self.len = 5
	
	@property
	def head(self):
		return self.snake[0]

	def eat(self):
		self.len += 3


	def update(self):
		vel = self.veldir.value * self.speed
		head = self.head + vel
		if head.x > width or head.x < 0:
			head.x %= width
		
		if head.y > height or head.y < 0:
			head.y %= height
		
		self.snake.insert(0, head)

		if (len(self.snake) > self.len):
			self.snake.pop()

	def turn(self, direction : Direction):
		if self.veldir.value != -direction.value:
			self.veldir = direction

	def draw(self, win):
		for rect in self.snake:
			pygame.draw.rect(win, self.color, pygame.Rect(rect.x - size / 2, rect.y - size / 2, size, size))

