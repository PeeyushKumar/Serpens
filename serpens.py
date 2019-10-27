import pygame
import time


width = 600
height = 400

white = (255,255,255)
black = (0,0,0)

cube_size = 20
speed = 10
snake = []


class cube:
	def __init__(self, color):
		self.corx = 0
		self.cory = 0
		self.color = color
		self.direction = "stop"

	def move(self, corx, cory):
		self.corx = corx
		self.cory = cory
		win.fill(white)
		pygame.draw.rect(win, self.color, (corx,cory,cube_size,cube_size))




def head_move():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		keys = pygame.key.get_pressed()

		for key in keys:
			if keys[pygame.K_UP]:
				head.direction = "up"
			if keys[pygame.K_DOWN]:
				head.direction = "down"
			if keys[pygame.K_LEFT]:
				head.direction = "left"
			if keys[pygame.K_RIGHT]:
				head.direction = "right"

	if head.direction == "up":
		head.move(head.corx, head.cory - speed)
	if head.direction == "down":
		head.move(head.corx, head.cory + speed)
	if head.direction == "left":
		head.move(head.corx - speed, head.cory)
	if head.direction == "right":
		head.move(head.corx + speed, head.cory)




pygame.init()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Serpens")

head = cube(black)
head.move(300,200)



run = True
while run:
	head_move()
	pygame.display.update()
	time.sleep(0.03)
	