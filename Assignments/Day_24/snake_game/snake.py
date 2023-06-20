from turtle import Turtle

# Create constant references
SNAKE_GRAVEYARD = 1200, 1200
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """
        Initialize the Snake class.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create the initial snake by creating turtle segments and positioning them.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Iterate over the starting positions list
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(SNAKE_GRAVEYARD)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a new segment to the end of the snake when it eats food
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move the snake by updating the positions of each segment.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Turn the snake to move up
        """
        # If not heading down, the snake can move up
        if self.head.heading() != DOWN:
            # Set the current heading of the snake's head
            self.head.setheading(UP)

    def down(self):
        """
        Turn the snake to move down
        """
        # If not heading up, the snake can move down
        if self.head.heading() != UP:
            # Set the current heading of the snake's head
            self.head.setheading(DOWN)

    def left(self):
        """
        Turn the snake to move left
        """
        # If not heading right, the snake can move left
        if self.head.heading() != RIGHT:
            # Set the current heading of the snake's head
            self.head.setheading(LEFT)

    def right(self):
        """
        Turn the snake to move right
        """
        # If not heading left, the snake can move right
        if self.head.heading() != LEFT:
            # Set the current heading of the snake's head
            self.head.setheading(RIGHT)

    def exit_program(self):
        """
        Exit the program with the space bar
        """
        self.head.screen.bye()

