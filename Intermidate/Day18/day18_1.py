import turtle
from turtle import Screen as s, Turtle as t
import random

tim = t()
turtle.colormode(255)
tim.shape("square")
tim.color("green")
tim.pensize(5)
tim.width(5)
tim.speed(10)
def random_color():
  r = random.randint(0, 255)
  b = random.randint(0, 255)
  g = random.randint(0, 255)
  random_color=(r,b,g)
  return random_color

for _ in range(50):
  tim.color(random_color())
  tim.right(random.randint(0,360))
  tim.forward(random.randint(30,50))
  tim.left(random.randint(0,360))  
  tim.forward(random.randint(30,100))
screen = s()
screen.exitonclick()
