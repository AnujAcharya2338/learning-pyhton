from turtle import Turtle as t, Screen as s

tim=t()
screen = s()

def move():
    tim.forward(10)
    
def back():
    tim.backward(10)
  
def right():
    tim.right(10)
      
def left():
    tim.left(10)
def clear():
    tim.home()
    tim.clear()
screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

