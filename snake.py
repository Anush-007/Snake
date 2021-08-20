from .vector import Vector
from enum import Enum
from random import choice

class Direction(Enum):
	left = Vector(-1, 0)
	right = Vector(1, 0)
	up = Vector(0, -1)
	down = Vector(0, 1)

class Snake():
	def __init__(self, start, body = [], speed = 10) -> None:
		self.head = Vector(*start)
		self.body = body
		self.speed = speed
		self.veldir = choice(list(Direction))

	def eat():
		pass

	def turn(self, direction : Direction):
		if self.veldir != -direction:
			self.veldir = direction
