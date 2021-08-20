# this is not for the snake game , may be for another like space invaders or, hurdle cross, or silimar obstacle based games


import pygame
from random import randint
from package.constants import *
from package.snake import Direction, Snake

pygame.init()



win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)


game_exit = False
game_over = False

clock = pygame.time.Clock()


def game_loop():

	snake = Snake((randint(0, width), randint(0, height)), speed = 3)
	# inc_speed = False


	game_exit_condition = game_exit
	while not game_exit_condition:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit_condition = True
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					snake.turn(Direction.up)
				
				elif event.key == pygame.K_DOWN:
					snake.turn(Direction.down)

				elif event.key == pygame.K_LEFT:
					snake.turn(Direction.left)
				
				elif event.key == pygame.K_RIGHT:
					snake.turn(Direction.right)
				

				# # the speed controls, Well I just wanted to do it, its coool.
				# elif event.key == pygame.K_SPACE:
				# 	pygame.key.set_repeat(15)
				# 	# snake.speed //= 2
				# 	if snake.speed > 4:
				# 		snake.speed -= 2

				# elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
				# 	pygame.key.set_repeat(15)
				# 	if snake.speed < 20:
				# 		snake.speed += 2
			


		if snake.speed < 8:
			snake.speed += 1
		elif snake.speed > 12:
			snake.speed -= 1

		snake.update()
		win.fill((0, 0, 0))

		pygame.draw.rect(win, (233, 50, 44), pygame.Rect(snake.head.x, snake.head.y, snake.size, snake.size))
		pygame.display.update()
		clock.tick(fps)


		




		

game_loop()


pygame.quit()

quit()



