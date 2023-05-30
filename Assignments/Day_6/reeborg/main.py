def turn_around():
    # Function to turn around by calling turn_left twice
    turn_left()
    turn_left()

def turn_right():
    # Function to turn right by calling turn_left three times
    for _ in range(3):
        turn_left()

def make_square_counterclockwise():
    # Function to make a square counterclockwise
    for _ in range(4):
        move()
        turn_left()

def make_square_clockwise():
    # Function to make a square clockwise
    for _ in range(4):
        move()
        turn_right()

def hurdle():
    # Function to jump over a hurdle
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# Call make_square_counterclockwise function
# make_square_counterclockwise()

# Call make_square_clockwise function
# make_square_clockwise()

# Call hurdle function 6 times
# for _ in range(6):
#     hurdle()

# Hurdle 1
# num_hurdles = 6

# while num_hurdles > 0:
#     hurdle()
#     num_hurdles -= 1
#     print(num_hurdles)

# Hurdle 2
# while not at_goal():
#     hurdle()

# Hurdle 3
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         hurdle()

# Hurdle 4
while not at_goal():
    if front_is_clear():
        move()
    else:
        hurdle()
