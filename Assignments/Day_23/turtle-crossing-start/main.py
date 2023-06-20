"""
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On
    the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.
"""
import time
from turtle import Screen
from player import Player
import car_manager
from car_manager import CarManager
from scoreboard import Scoreboard


GAME_BOARD_COLOR = "#1F3B4D"

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor(GAME_BOARD_COLOR)

# Instantiate the player
player = Player()

#TODO Car Generation: Create a new car at random time intervals but not have more 3 cars generated at a time
# time_interval = 0
# while time_interval < 10:
cars = []

for _ in range(15):
    # Instantiate the car
    new_car = CarManager()
    cars.append(new_car)
    # time_interval += 1

# Instantiate the scoreboard
scoreboard = Scoreboard()


# Event listeners
screen.listen()
screen.onkey(player.go_up, "Up")

# Exit on space bar for development
def exit_program():
    """
    Exit the program with the space bar
    """
    screen.bye()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()

    # car.generate_car()



    # Exit on space bar for development
    screen.onkeypress(exit_program, "space")
