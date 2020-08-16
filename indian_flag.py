import turtle

t = turtle.Turtle()
t.speed(5)
# to move the coordinates 
def move(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()

t.pensize(3)

# Ashok Chakra
t.color('#000080')
for i in range(24):
	t.forward(70)
	t.backward(70)
	t.left(15)

t.pensize(6)
move(0, -70)
t.circle(70, 360)

# Green (Lower Part)
t.pensize(2)
t.color('#138808')
t.fillcolor('#138808')
t.begin_fill()

move(0, -90)

t.forward(300)
t.right(90)

t.forward(150)
t.right(90)

t.forward(600)
t.right(90)

t.forward(150)
t.right(90)

t.forward(300)

t.end_fill()

# Saffron (Upper part)
t.color('#FF9933')
t.fillcolor('#FF9933')
t.begin_fill()

move(0, 90)

t.forward(300)
t.left(90)

t.forward(150)
t.left(90)

t.forward(600)
t.left(90)

t.forward(150)
t.left(90)

t.forward(300)

t.end_fill()

t.hideturtle()

turtle.done()
