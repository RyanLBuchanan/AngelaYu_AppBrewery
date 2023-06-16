import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Even listeners
def move_forwards():
    tim.forward(10)

screen.listen()

#Function as input
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()