def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for _ in range(3):
        turn_left()


def make_square_counterclockwise():
    for _ in range(4):
        move()
        turn_left()


def make_square_clockwise():
    for _ in range(4):
        move()
        turn_right()


def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# Call make_square_counterclockwise function
# make_square_counterclockwise()

# Call make_square_clockwise function
# make_square_clockwise()

# Call hurdle function 6 times
# for _ in range(6):
#     hurdle()

# num_hurdles = 6

# while num_hurdles > 0:
#     hurdle()
#     num_hurdles -= 1
#     print(num_hurdles)

while not at_goal():
    hurdle()