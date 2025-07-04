from turtle import Screen 
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.snake[0].distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.increase_score()
        snake.increase()

    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        game_is_on = False
        scoreboard.gameover()
    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) <10:
            game_is_on = False
            scoreboard.gameover()
            
screen.exitonclick()