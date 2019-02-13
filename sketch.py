from turtle import *

screen = Screen()
screen.title("Turtle Sketcher")
screen.bgcolor("#268e30")

troy = Turtle()
troy.color("#1a5166")
troy.pensize(5)
troy.speed(2)
troy.shape("turtle")

def go_up():
	troy.setheading(90)
	troy.forward(10)

def go_down():
	troy.setheading(270)
	troy.forward(10)

def go_right():
	troy.setheading(0)
	troy.forward(10)

def go_left():
	troy.setheading(180)
	troy.forward(10)

def draw_star():
	screen.onkeypress(None, "Up")
	screen.onkeypress(None, "Down")
	screen.onkeypress(None, "Left")
	screen.onkeypress(None, "Right")
	troy.color("red")
	for x in range(5):
		troy.forward(50)
		troy.left(144)
	troy.color("#1a5166")

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(draw_star, "z")

screen.listen()

mainloop()