from .vector import Vector
from enum import Enum, auto

class Direction(Enum):
	left = auto()
	right = auto()
	up = auto()
	down = auto()

class Snake():
	def __init__(self, start, body = []) -> None:
		self.head = Vector(*start)
		self.body = body

	def eat():
		pass

	def turn():
		pass