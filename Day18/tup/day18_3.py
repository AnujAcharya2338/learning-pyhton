from turtle import Screen as s, Turtle as t
from turtle import colormode

import colorgram as cg
import random
# color_list = cg.extract("C:/Users/USER/Downloads/day-1-printing-start/Day18/tup/a.jpg", 60)
# color_palete=[]

# for color in color_list:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     color_palete.append(new_color)
# print(color_palete)
colormode(255)

rows=10
columns=10
gap = 50
dot_size = 20

color_list=[(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 
10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]


tim= t()
tim.hideturtle()
tim.penup()
start_x = -columns * gap // 2
start_y = -rows * gap // 2

for row in range(rows):
    for cols in range(columns):
        x = start_x + cols * gap
        y = start_y + row * gap
        tim.goto(x,y)
        tim.dot(dot_size, random.choice(color_list))
    

screen= s()
screen.exitonclick()
