import pygame
from random import randint
from package.constants import *
from package.snake import Direction, Snake
from package.food import Food

pygame.init()



win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)


game_exit = False
game_over = False

clock = pygame.time.Clock()


def game_loop():

	snake = Snake((randint(0, width), randint(0, height)), speed = 10)
	food = Food()

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
		
		

		snake.update()
		win.fill((0, 0, 0))
		
		if abs(food.x - snake.head.x) < size / 2 + 1 and abs(food.y - snake.head.y) < size / 2 + 1:
			snake.eat()
			food = Food()

		food.draw(win)
		snake.draw(win)

		pygame.display.update()
		clock.tick(fps)


		




		

game_loop()


pygame.quit()

quit()



