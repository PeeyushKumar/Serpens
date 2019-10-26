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
head.shapesize(1,1)
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"


while True:
	win.update()
	time.sleep(0.1)

turtle.mainloop()