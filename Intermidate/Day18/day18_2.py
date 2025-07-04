import turtle as t
import random

myturtle = t.Turtle()
t.colormode(255)
myturtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        myturtle.color(random_color())
        myturtle.circle(100)
        myturtle.setheading(myturtle.heading() + size_of_gap)

draw_spirograph(10)
screen = t.Screen()
screen.exitonclick()