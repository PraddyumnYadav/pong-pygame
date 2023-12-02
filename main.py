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


def draw(w_circle: int, bar1, bar2, line, circle_x, circle_y):
	# Draw Circle(Ball)
	pygame.draw.circle(WIN, "white", (circle_x, circle_y), w_circle)

	# Draw Bars
	pygame.draw.rect(WIN, "white", bar1)
	pygame.draw.rect(WIN, "white", bar2)

	# Draw Line in the Middle (Separation Line)
	pygame.draw.rect(WIN, "white", line)

	# Update the Display
	pygame.display.update()


def main():
	run = True

	circle_x = int(WIDTH/2)
	circle_y = int(HEIGHT/2)

	ball_vel = 1
	bar_vel = 5

	line = pygame.Rect(int(WIDTH/2-LINE_WIDTH/2), 0, LINE_WIDTH, HEIGHT)
	bar1 = pygame.Rect(10, circle_y, BAR_WIDTH, BAR_HEIGHT)
	bar2 = pygame.Rect(
		int(WIDTH-BAR_WIDTH-10),
		int(HEIGHT-BAR_HEIGHT-10),
		BAR_WIDTH,
		BAR_HEIGHT
	)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw(CIRCLE_WIDTH, bar1, bar2, line, circle_x, circle_y)
		circle_x += ball_vel
		circle_y += ball_vel

		bar1.y = circle_y



if __name__ == "__main__":
	main()
