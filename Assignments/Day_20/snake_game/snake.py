from turtle import Turtle

# Create a constant reference
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# The starting positions for each segment of the snake. Adjust the values as needed.
# List comprehension for the above list: [n * -20 for n in range(3)]
# -> new_segment.goto(x=starting_positions[position], y=0)
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        """
        Initialize the Snake class.
        """
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """
        Create the initial snake by creating turtle segments and positioning them.
        """
        for position in STARTING_POSITIONS:
            # Iterate over the starting positions list
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """
        Move the snake by updating the positions of each segment.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Turn the snake to move up
        """
        # Get the current heading of the snake's head
        current_heading = self.segments[0].heading()

        # Check if the snake is already moving vertically
        if current_heading != 90 and current_heading != 270:
            # Set the new heading to up (0 degrees)
            self.segments[0].setheading(0)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].left(90)

    def down(self):
        """
        Turn the snake to move down
        """
        # Get the current heading of the snake's head
        current_heading = self.segments[0].heading()

        # Check if the snake is already moving vertically
        if current_heading != 90 and current_heading != 270:
            # Set the new heading to up (0 degrees)
            self.segments[0].setheading(0)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].right(90)

    def left(self):
        """
        Turn the snake to move left
        """
        # Get the current heading of the snake's head
        current_heading = self.segments[0].heading()

        # Check if the snake is already moving vertically
        if current_heading != 90 and current_heading != 270:
            # Set the new heading to up (0 degrees)
            self.segments[0].setheading(0)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].left(90)

    def right(self):
        """
        Turn the snake to move right
        """
        # Get the current heading of the snake's head
        current_heading = self.segments[0].heading()

        # Check if the snake is already moving vertically
        if current_heading != 90 and current_heading != 270:
            # Set the new heading to up (0 degrees)
            self.segments[0].setheading(0)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].right(90)

    def exit_program(self):
        """
        Exit the program with the space bar
        """
        self.segments[0].screen.bye()

