from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = (0,-230)

class Tartaruga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.reset_position()
        self.setheading(90)
        self.speed("fast")

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)