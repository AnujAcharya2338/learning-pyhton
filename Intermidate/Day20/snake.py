from turtle import Turtle
STARTING_POSITION=[0,-20,-40]
MOVEMENT = 20
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
        self.snake[0].setheading(90)
    def down(self):
        self.snake[0].setheading(270)
    def left(self):
        self.snake[0].setheading(180)
    def right(self):
        self.snake[0].setheading(0)