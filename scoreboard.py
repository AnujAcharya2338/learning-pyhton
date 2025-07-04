from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        data= open ("data.txt") 
        self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        data.close()
        
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore} ", align="center", font=("Courier",16,"bold"))
        
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            data=open("data.txt", mode="w")
            data.write(f"{self.highscore}")
            data.close()
            
        self.score=0
        self.update_score()
        
    
    def increase_score(self):
        self.score +=1
        self.update_score()