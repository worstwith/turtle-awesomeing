import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
for i in range(6):
    polygon.forward(100)
    polygon.right(60)
polygon.penup()
polygon.goto(-25,30)
polygon.pendown()
for i in range(6):
    polygon.forward(100)
    polygon.left(60)
