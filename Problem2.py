from turtle import *

screen = Screen()
screen.title("Turtle Sketcher")
screen.bgcolor("#9b7c26")

chad = Turtle()
chad.color("#563313")
chad.pensize(5)
chad.speed(2)
chad.shape("turtle")

def go_right():
	chad.setheading(0)
	chad.forward(10)

def go_up():
	chad.setheading(90)
	chad.forward(10)

def go_left():
	chad.setheading(180)
	chad.forward(10)

def go_down():
	chad.setheading(270)
	chad.forward(10)

def draw_square():
	screen.onkeypress(None, "Right")
	screen.onkeypress(None, "Up")
	screen.onkeypress(None, "Left")
	screen.onkeypress(None, "Down")
	chad.color("#9b7c26")
	for x in range(4):
		chad.forward(40)
		chad.left(90)
	chad.color("#563313")

screen.onkeypress(go_right, "Right")
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_down, "Down")
screen.onkeypress(draw_square, "q")

screen.listen()

mainloop()