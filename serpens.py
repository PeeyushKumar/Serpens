import turtle
import time

# Setting up the screen
win = turtle.Screen()
win.setup()
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

# Head movement
def move():
	x = 0
	y = 0
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 5)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 5)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 5) 
	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 5)

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


# Main loop
while True:
	win.update()
	time.sleep(0.03)
	move()

turtle.mainloop()