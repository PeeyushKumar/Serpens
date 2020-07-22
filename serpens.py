import pygame
import time
import random
import math
import os
import pickle

#Variables
width = 600
height = 400

l_edge = 0
r_edge = width
u_edge = 0
d_edge = height

white = (225,225,225)
black = (0,0,0)
red = (255,0,0)
grey = (175,175,175)

cube_size = 20
speed = 10
snake = []


#Snake blocks class
class cube:
	def __init__(self, color):
		self.color = color
		self.corx = (width + cube_size)/2
		self.cory = (height + cube_size)/2
		self.direction = "stop"
		self.move(self.corx,self.cory)

	def move(self, corx, cory):
		self.corx = corx
		self.cory = cory
	
	def draw(self):
		pygame.draw.rect(win, self.color, (self.corx,self.cory,cube_size,cube_size))


#Food class
class create_food:
	def __init__(self, color):
		self.corx = random.randint(l_edge, r_edge - cube_size)
		self.cory = random.randint(u_edge, d_edge - cube_size)
		self.color = color

	def draw(self):
		pygame.draw.ellipse(win, self.color, (self.corx,self.cory,cube_size,cube_size))

	def jump(self):
		self.corx = random.randint(l_edge, r_edge - cube_size)
		self.cory = random.randint(u_edge, d_edge - cube_size)


#Movement
def head_move():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		keys = pygame.key.get_pressed()

		for key in keys:
			if keys[pygame.K_UP] and head.direction != "down":
				head.direction = "up"
			if keys[pygame.K_DOWN] and head.direction != "up":
				head.direction = "down"
			if keys[pygame.K_LEFT] and head.direction != "right":
				head.direction = "left"
			if keys[pygame.K_RIGHT] and head.direction != "left":
				head.direction = "right"
			if keys[pygame.K_r]:
				hi_score = 0
				with open("data", "wb") as file:
					pickle.dump(hi_score, file)

	if head.direction == "up":
		head.move(head.corx, head.cory - speed)
	if head.direction == "down":
		head.move(head.corx, head.cory + speed)
	if head.direction == "left":
		head.move(head.corx - speed, head.cory)
	if head.direction == "right":
		head.move(head.corx + speed, head.cory)

def body_move():
	for index in range(len(snake)-1,0,-1):
		snake[index].move(snake[index-1].corx, snake[index-1].cory)
	if len(snake) > 0:
		snake[0].move(head.corx, head.cory)

		
#Draw serpent
def draw_snake():
	for part in snake:
		part.draw()
	head.draw()


#Food collision
def eat():
	food.draw()
	if math.sqrt(((food.corx - head.corx)**2)+((food.cory - head.cory)**2)) < cube_size:
		food.jump()
		food.draw()

		part = cube(grey)
		snake.append(part)


#Scoring
def calc_score():
	score = len(snake)*10

	font = pygame.font.Font('freesansbold.ttf', 32)

	text= font.render("Score: " + str(score), True, black, white) 
	textRect = text.get_rect()  
	textRect.center = (width // 2, height // 2)
	win.blit(text, textRect)

	if os.path.isfile("data"):
		with open("data", "rb") as file:
			hi_score = pickle.load(file)
		if score > hi_score:
			hi_score = score
			with open("data", "wb") as file:
				pickle.dump(hi_score, file)
			text = font.render("New Highscore", True, black, white)
			textRect = text.get_rect() 
			textRect.center = (width // 2, height // 2 + 50)
			win.blit(text, textRect)
	else:
		hi_score = score
		with open("data", "wb") as file:
			pickle.dump(hi_score, file)
	
	pygame.display.update()


#Collision
def reset():
	head.direction = "stop"
	calc_score()
	for index in range(len(snake)):
		del snake[0]
	head.move((width + cube_size)/2, (height + cube_size)/2)
	food.jump()
	time.sleep(2)


def check_collision():
	if head.corx == l_edge or head.corx == r_edge-cube_size:	
		reset()

	elif head.cory == u_edge or head.cory == d_edge-cube_size:
		reset()

	else:
		for index in range(0, len(snake)):
			if math.sqrt(((snake[index].corx - head.corx)**2)+((snake[index].cory - head.cory)**2)) < cube_size/2:
				reset()
				break



#Game window
pygame.init()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Serpens")
head = cube(black)
food = create_food(red)



#Game loop
run = True
while run:
	win.fill(white)
	eat()
	body_move()
	head_move()
	draw_snake()
	pygame.display.update()
	check_collision()
	time.sleep(0.02)