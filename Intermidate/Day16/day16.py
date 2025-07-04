# from turtle import Turtle, Screen
# ram = Turtle()
# print(ram)
# ram.shape("turtle")
# ram.color("red")
# ram.forward(100)
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column(
    "Pokemon Name",
    [
        "Pikachu",
        "Onion Turtle",
        "Punchy Rock",
        "Floor shit",
        "Ground shit",
        "3 Floor shit",
        "Big Deep Bee",
    ],
)
table.add_column(
    "Pokemon Type",
    [
        "Chinese",
        "Arnold",
        "Stuck ",
        "In",
        "Hog ",
        "Rider's",
        "Crack ",
    ],
)
table.align="l"
print(table)
