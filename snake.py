from turtle import Turtle
STARTING_POSITION=[(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP = 90
DOWN=270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)
    
    def add_snake(self, position):
            half_snake=Turtle()
            half_snake.shape("square")
            half_snake.color("white")
            half_snake.penup()
            half_snake.goto(position)
            self.snake.append(half_snake)
            
    def increase(self):
            self.add_snake(self.snake[-1].position())
            
            
    def move(self):   
        for seg in range(len(self.snake)-1,0,-1):
            x_cordinate=self.snake[seg-1].xcor()
            y_cordinate=self.snake[seg-1].ycor()
            self.snake[seg].goto(x_cordinate,y_cordinate)
        self.snake[0].forward(MOVEMENT)
        
     
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]
        
        
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
     
