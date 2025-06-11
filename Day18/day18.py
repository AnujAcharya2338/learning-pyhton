from turtle import Screen as s, Turtle as t
import random
tim = t()
tim.shape("turtle")
tim.color("red")

colors = ["pale green", "aquamarine", "orange red" , "saddle brown", "goldenrod" ,"light sea green","deep sky blue","salmon","dark goldenrod","dark slate blue"]
def shape(num_side):
  for _ in range(num_side):
   angle=360/num_side
   tim.forward(70)
   tim.left(angle)
 
 
for num_size in range(3,11):
     tim.color(random.choice(colors))
     shape(num_size)
screen = s()
screen.exitonclick()
