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

# Exit program on space bar key press
def exit_program():
    """
    Exit the program with the space bar
    """
    screen.bye()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "name?").title()

    all_states = data.state.to_list()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If the answer state is one of the states
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# # Bind the exit program function to the space bar
# screen.onkeypress(exit_program, "space")

# # Close the screen when clicked
# screen.exitonclick()


# def get_mouse_click_coordinates(x, y):
#     """
#     Get the x and y coordinates of a mouse click on the screen
#     """
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)  # Bind the function to mouse click events
#
# turtle.mainloop()

