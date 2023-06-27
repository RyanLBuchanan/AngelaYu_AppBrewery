import turtle as t
import random

tim = t.Turtle()

# Increase the pensize by a factor of 10
tim.pensize(tim.pensize() * 10)

# Make turtle walk faster
tim.speed(10)

# Set the directions for the random walk
directions = [0, 90, 180, 270]

# Set the color mode
t.colormode(255)

# Choose random color
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Return a random color tuple
    random_color = (r, g, b)
    return random_color


for _ in range(200):
    tim.color(get_random_color())
    tim.forward(25)
    tim.setheading(random.choice(directions))
