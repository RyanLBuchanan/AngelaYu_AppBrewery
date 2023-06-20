import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


GAME_BOARD_COLOR = "#32c18f"

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor(GAME_BOARD_COLOR)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
