from turtle import *

screen = Screen()
screen.title("Turtle Sketcher")
screen.bgcolor("#5e8aa5")

gabriella = Turtle()
gabriella.color("#88178c")
gabriella.pensize(5)
gabriella.speed(2)
gabriella.shape("turtle")

def go_up():
	gabriella.setheading(90)
	gabriella.forward(10)

def go_down():
	gabriella.setheading(270)
	gabriella.forward(10)

def go_right():
	gabriella.setheading(0)
	gabriella.forward(10)

def go_left():
	gabriella.setheading(180)
	gabriella.forward(10)

def draw_star():
	screen.onkeypress(None, "Up")
	screen.onkeypress(None, "Down")
	screen.onkeypress(None, "Left")
	screen.onkeypress(None, "Right")
	gabriella.color("purple")
	for x in range(5):
		gabriella.forward(50)
		gabriella.left(144)
	gabriella.color("#88178c")

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(draw_star, "z")

screen.listen()

mainloop()