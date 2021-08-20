from snake import Snake
import pygame
from random import randint
from .constants import *

pygame.init()



win = pygame.display.set_mode((widht, height))
pygame.display.set_caption(title)


game_exit = False
game_over = False



def game_loop():

	snake = Snake((randint()))
	game_exit_condition = game_exit
	while not game_exit_condition:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit_condition = True

		




		

game_loop()


pygame.quit()

quit()



