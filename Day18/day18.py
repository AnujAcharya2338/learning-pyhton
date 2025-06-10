from turtle import Screen as s, Turtle as t

tim = t()
tim.shape("turtle")
tim.color("red")

for _ in range(50): 
     
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.pendown()
screen = s()
screen.exitonclick()
