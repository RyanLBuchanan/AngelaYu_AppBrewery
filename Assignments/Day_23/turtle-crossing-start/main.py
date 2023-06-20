import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


GAME_BOARD_COLOR = "#1F3B4D"

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor(GAME_BOARD_COLOR)

# Instantiate the player
player = Player()
car_manager = CarManager()

cars = []
for _ in range(15):
    # Instantiate the car
    new_car = CarManager()
    cars.append(new_car)

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

    car_manager.create_car()

    car_manager.move_cars()

    # Detect collisions with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Exit on space bar for development
    screen.onkeypress(exit_program, "space")

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
