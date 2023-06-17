from turtle import Turtle


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
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        # The starting positions for each segment of the snake. Adjust the values as needed.
        # List comprehension for the above list: [n * -20 for n in range(3)]
        # -> new_segment.goto(x=starting_positions[position], y=0)
        for position in starting_positions:
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
        self.segments[0].forward(20)
