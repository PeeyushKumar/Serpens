import turtle
import time
import random

body = []

r_edge = 290
l_edge = -290
u_edge = 165
d_edge = -190


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
	if head.xcor() > r_edge or head.xcor() < l_edge or head.ycor() > u_edge or head.ycor() < d_edge:
		reset()

	for part in body:
		if head.distance(part) < 15:
			reset()

# Scoring
pen = turtle.Turtle()
pen.color("black")
pen.shapesize(1)
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.pensize(1)
pen.goto(0,170)


def scoreboard():
	pen.clear()
	score = len(body)*10
	pen.write("Score:" + str(score), False, align="center", font=("Roboto", 15, "normal"))

# Drawing border
pen2 = turtle.Turtle()
pen2.color("black")
pen2.shapesize(1)
pen2.speed(0)
pen2.hideturtle()
pen2.pensize(2)
pen2.penup()
pen2.goto(l_edge, u_edge)
pen2.pendown()

def draw_border():
	pen2.goto(r_edge,u_edge)
	pen2.goto(r_edge, d_edge)
	pen2.goto(l_edge, d_edge)
	pen2.goto(l_edge, u_edge)


# Main loop
while True:

	scoreboard()

	draw_border()

	#Serpent eating food
	if head.distance(food) < 15:
		x = random.randint(l_edge + 20, r_edge - 20)
		y = random.randint(d_edge + 20, u_edge -20)
		food.goto(x,y)

		#Add a new part
		part = turtle.Turtle()
		part.penup()
		part.speed(5)
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