import turtle
import pandas as pd

# Create a turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load and set the background image
image = "blank_states_img.gif"
screen.addshape(image)
screen.bgcolor("#1F3B4D")
turtle.shape(image)

# Load the data of U.S. states from a CSV file
data = pd.read_csv("50_states.csv")


def exit_program():
    """
    Exit the program with the space bar
    """
    screen.bye()


def get_mouse_click_coordinates(x, y):
    """
    Get the x and y coordinates of a mouse click on the screen
    """
    print(x, y)


# Event listeners
screen.listen()  # Start listening for events
turtle.onscreenclick(get_mouse_click_coordinates)  # Bind the function to mouse click events
screen.onkeypress(exit_program, "space")  # Bind the exit program function to the space bar

# Close the screen when clicked
screen.exitonclick()
