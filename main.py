# -----------------------Pong Game with Python and Pygame----------------------- #
import os
import pygame

# Setting Global Parameters
WIDTH, HEIGHT = 800, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Praddyumn Yadav")


def main():
	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


if __name__ == "__main__":
	main()
