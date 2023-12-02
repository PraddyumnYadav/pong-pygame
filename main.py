# -----------------------Pong Game with Python and Pygame----------------------- #
import os
import pygame

# Setting Global Parameters
WIDTH, HEIGHT = 800, 675
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Praddyumn Yadav")

BAR_HEIGHT = 225
BAR_WIDTH = 25
CIRCLE_WIDTH = 35
LINE_WIDTH = 10


def draw(w_circle: int, bar1, bar2, line):
	# Draw Circle(Ball)
	pygame.draw.circle(WIN, "white", (int(WIDTH/2), int(HEIGHT/2)), w_circle)

	# Draw Bars
	pygame.draw.rect(WIN, "white", bar1)
	pygame.draw.rect(WIN, "white", bar2)

	# Draw Line in the Middle (Separation Line)
	pygame.draw.rect(WIN, "white", line)

	# Update the Display
	pygame.display.update()


def main():
	run = True
	bar1 = pygame.Rect(10, 10, BAR_WIDTH, BAR_HEIGHT)
	bar2 = pygame.Rect(
		int(WIDTH-BAR_WIDTH-10),
		int(HEIGHT-BAR_HEIGHT-10),
		BAR_WIDTH,
		BAR_HEIGHT
	)
	line = pygame.Rect(int(WIDTH/2-LINE_WIDTH/2), 0, LINE_WIDTH, HEIGHT)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw(CIRCLE_WIDTH, bar1, bar2, line)


if __name__ == "__main__":
	main()
