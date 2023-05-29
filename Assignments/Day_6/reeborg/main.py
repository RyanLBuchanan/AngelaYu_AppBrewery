def turn_around():
    turn_left()
    turn_left()


def turn_right_around():
    turn_around()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def make_square_counterclockwise():
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()


def make_square_clockwise():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


# make_square_clockwise()
# make_square_counterclockwise()

