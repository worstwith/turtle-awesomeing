import turtle
turtle.Screen().bgcolor("DarkOrchid1")
turtle.Screen().setup(300,400)
turtle.title("What in the THREE MOONS")
moon = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        moon.fd(size+1)
        moon.left(90)
        size = size - 1
    size = size + 0.5
#Are you ready!# makes an optical illusion