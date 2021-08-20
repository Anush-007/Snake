

# this will be used as a container for 2D values including the position and speed for the snake

class Vector :
	def __init__(self, x, y):
		self.__tup = [x, y]

	@property
	def x(self) :
		return self.__tup[0]
	
	@property
	def y(self) :
		return self.__tup[1]

	@x.setter
	def x(self, x):
		self.__tup[0] = x

	@y.setter
	def y(self, y):
		self.__tup[1] = y

	def __add__(self, other) :
		return Vector(self.x + other.x, self.y + other.y)
	
	def __iadd__(self, other) :
		self.x += other.x
		self.y += other.y
		return self
	
	def __mul__(self, other : float) :
		return Vector(other * self.x, other * self.y)

	def __imul__(self, other):
		self.x *= other
		self.y *= other
		return self

	def __neg__(self):
		return Vector(-self.x, -self.y)
	
	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)
	
	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __ne__(self, other):
		return self.x != other.x or self.y != other.y

	def add(self, other):
		self.x += other.x
		self.y += other.y

	def sub(self, other):
		# self -= other # Either this can be done or what is done below
		self.x -= other.x
		self.y -= other.y



# if __name__ == '__main__':
# 	print(Vector(3, 7)._Vector__tup)
# 	print(Vector(3, 2).x)