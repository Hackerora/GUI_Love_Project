import turtle

turtle.speed(2)
turtle.bgcolor("black")
turtle.pensize(5)
turtle.color("red", "purple")

def draw():
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)

    for _ in range(200):
        turtle.right(1)
        turtle.forward(1)

    turtle.left(120)

    for _ in range(200):
        turtle.right(1)
        turtle.forward(1)

    turtle.forward(120)
    turtle.end_fill()
    
draw()
turtle.hideturtle()
turtle.done()