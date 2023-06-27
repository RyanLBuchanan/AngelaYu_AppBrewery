import turtle as t
import random
import math

tim = t.Turtle()

# Increase the pensize by a factor of 10
# tim.pensize(tim.pensize() * 10)

# Make turtle walk faster
tim.speed(10 * 50)

# Set the directions for the random walk
directions = [0, 90, 180, 270]

# Set the color mode
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

# Choose random color
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Return a random color tuple
    random_color = (r, g, b)
    return random_color

def draw_spirograph(R, r, d, rotations):
    # R: radius of the large circle
    # r: radius of the small circle
    # d: distance from the small circle's center to the pen
    # Calculate the number of rotations needed to complete the spirograph
    # Set the radii of the large and small circles


    # Calculate the number of rotations needed to complete the spirograph
    # rotations = 360 // math.gcd(R, r)

    for _ in range(rotations):
        tim.color(get_random_color())  # Set pen color of inner (invisible) circle
        tim.circle(R)  # Draw a circle with radius of R
        tim.color(get_random_color())  # Set random pen color of outer circle
        tim.circle(r, 360) # Draw a circle with radius of r
        tim.left(d)  # Turn left by angle of d


# Call the spirograph function
draw_spirograph(150, 50, 5, 100)