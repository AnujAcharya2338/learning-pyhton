from turtle import Screen ,Turtle
from snake import Snake
import time
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
snake=[]
x_axis=[0,-20,-40]
for position in range(0,3):
    half_snake=Turtle()
    half_snake.shape("square")
    half_snake.color("white")
    half_snake.penup()
    half_snake.goto(x=x_axis[position],y=0)
    snake.append(half_snake)

game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg in range(len(snake)-1,0,-1):
        x_cordinate=snake[seg-1].xcor()
        y_cordinate=snake[seg-1].ycor()
        snake[seg].goto(x_cordinate,y_cordinate)
    snake[0].forward(20)







screen.exitonclick()