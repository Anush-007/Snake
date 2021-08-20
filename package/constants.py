width = 1280
height = 720

title = "Snake Game"

fps = 60


#snakes 

size = 10
square = (size, size)

#colours

def singleton(_class):
	instances = {}
	def getinstance(*args, **kwargs):
		if _class not in instances:
			instances[_class] = _class(*args, **kwargs)
		return instances[_class]
	return getinstance

@singleton
class Colors:
	white = (255, 255, 255)
	black = (0, 0, 0)




# colours = Colors() # this can be done if we don't use the singleton and just define a class , we can create an instance of class which will be the only instance of the class and hence will act just as a singleton

# speed bounds

# @singleton
# class SpeedBounds:
# 	upper = 20
# 	lower = 4