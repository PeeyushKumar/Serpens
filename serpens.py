import turtle
import time
import random

body = []


# Setting up the screen
win = turtle.Screen()
win.setup(width=600, height=400)
win.title("Serpens")
win.tracer(0)

# Creating serpent head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.shapesize(1)
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"


# Creating serpent food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(1)
food.speed(0)
food.penup()
food.goto(random.randint(-280, +280),random.randint(-180, +180))
food.direction = "stop"

# Head movement
def head_move():
	x = 0
	y = 0
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 15)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 15)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 15) 
	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 15)


def goup():
	if head.direction != "down":
		head.direction = "up"
def godown():
	if head.direction != "up":
		head.direction = "down"
def goleft():
	if head.direction != "right":
		head.direction = "left"
def goright():
	if head.direction != "left":
		head.direction = "right"

win.listen()
win.onkeypress(goup, "Up")
win.onkeypress(godown, "Down")
win.onkeypress(goleft, "Left")
win.onkeypress(goright, "Right")


# Body movement
def body_move():
	for index in range(len(body)-1,0,-1):
		body[index].setx(body[index-1].xcor())
		body[index].sety(body[index-1].ycor())
	if len(body) > 0:	
		body[0].setx(head.xcor())
		body[0].sety(head.ycor())


# Collision behaviour
def reset():
	head.direction = "stop"
	head.goto(0,0)
	for index in range(len(body)):
		body[index].goto(10000,10000)
	body.clear()


def check_collisions():
	if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 180 or head.ycor() < -180:
		reset()

	for part in body:
		if head.distance(part) < 15:
			reset()


# Main loop
while True:
	#Serpent eating food
	if head.distance(food) < 15:
		x = random.randint(-280, +280)
		y = random.randint(-180, +180)
		food.goto(x,y)

		#Add a new part
		part = turtle.Turtle()
		part.penup()
		part.speed(0)
		part.shape("square")
		part.color("grey")
		part.direction = "stop"
		body.append(part)

	
	body_move()
	
	head_move()

	check_collisions()
	

	win.update()
	time.sleep(0.05)

turtle.mainloop()