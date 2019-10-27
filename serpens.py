import pygame

white = (255,255,255)
black = (0,0,0)

cube_size = 20

class cube:
	def __init__(self, color):
		self.corx = 0
		self.cory = 0
		self.color = color
	def draw(self, corx, cory):
		pygame.draw.rect(win, self.color, (corx,cory,cube_size,cube_size))






pygame.init()

win = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Serpens")
win.fill((255,255,255))

run = True
while run:
	x = cube(black)
	x.draw(0,0)
	pygame.display.update()