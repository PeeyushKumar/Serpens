import turtle
import time
import random

#Variables
body = []

width = 800
height = 600

r_edge = width/2 - 10
l_edge = width*(-1)/2 +10
u_edge = height/2 - 35
d_edge = height*(-1)/2 +10


#Setting up the screen
win = turtle.Screen()
win.setup(width, height)
win.title("Serpens")
win.tracer(0)


#Drawing border
pen = turtle.Turtle()
pen.color("black")
pen.shapesize(1)
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

pen.penup()
pen.goto(l_edge, u_edge)
pen.pendown()
pen.goto(r_edge,u_edge)
pen.goto(r_edge, d_edge)
pen.goto(l_edge, d_edge)
pen.goto(l_edge, u_edge)


#Serpent head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.shapesize(1)
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"


#Serpent food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(1)
food.speed(0)
food.penup()
food.goto(random.randint(l_edge+20, r_edge-20),random.randint(d_edge+20, u_edge-20))

def	eat():
	if head.distance(food) < 15:
		x = random.randint(l_edge + 20, r_edge - 20)
		y = random.randint(d_edge + 20, u_edge - 20)
		food.goto(x,y)

		#Add a new part
		part = turtle.Turtle()
		part.penup()
		part.speed(0)
		part.shape("square")
		part.color("grey")
		body.append(part)


#Head movement
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


#Body movement
def body_move():
	for index in range(len(body)-1,0,-1):
		body[index].setx(body[index-1].xcor())
		body[index].sety(body[index-1].ycor())
	if len(body) > 0:	
		body[0].setx(head.xcor())
		body[0].sety(head.ycor())


#Collision behaviour
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

#Scoring
spen = turtle.Turtle()
spen.color("black")
spen.shapesize(1)
spen.speed(0)
spen.penup()
spen.hideturtle()
spen.pensize(1)
spen.goto(0,u_edge)

def scoreboard():
	spen.clear()
	score = len(body)*10
	spen.write("Score:" + str(score), False, align="center", font=("Roboto", 20, "normal"))


#Game loop
while True:
	scoreboard()
	eat()
	body_move()
	head_move()
	check_collisions()

	win.update()
	time.sleep(0.05)

turtle.mainloop()