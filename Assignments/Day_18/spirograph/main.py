import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# Create turtle screen
screen = t.Screen()
screen.setup(1000, 1000)


# Function for exiting turtle with space bar
def exit_program():
    t.bye()


# Bind the exit program to the space bar
screen.onkeypress(exit_program, "space")

# Enable listening for key events
screen.listen()


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Return a random color tuple
    random_color = (r, g, b)
    return random_color


# Set the speed of drawing to the fastest
tim.speed("fastest")

def draw_spirogrpah(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.color(get_random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirogrpah(5)
screen.exitonclick()
