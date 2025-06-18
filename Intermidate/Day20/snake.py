from turtle import Turtle
STARTING_POSITION=[0,-20,-40]
MOVEMENT = 20
UP = 90
DOWN=270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
    
    def create_snake(self):
        for position in range(0,3):
            half_snake=Turtle()
            half_snake.shape("square")
            half_snake.color("white")
            half_snake.penup()
            half_snake.goto(x=STARTING_POSITION[position],y=0)
            self.snake.append(half_snake)
        
    def move(self):   
        for seg in range(len(self.snake)-1,0,-1):
            x_cordinate=self.snake[seg-1].xcor()
            y_cordinate=self.snake[seg-1].ycor()
            self.snake[seg].goto(x_cordinate,y_cordinate)
        self.snake[0].forward(MOVEMENT)
    
    def up(self):
        if self.snake[0].heading() != DOWN:
          self.snake[0].setheading(UP)
    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)
    def right(self):
        if self.snake[0].heading() != LEFT:
             self.snake[0].setheading(RIGHT)