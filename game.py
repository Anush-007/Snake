import pygame

pygame.init()

win = pygame.display.set_mode((1000, 800))

pygame.display.set_caption("Snake Game")

game_exit = False
game_over = False



while not game_exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_exit = True


pygame.quit()

quit()



