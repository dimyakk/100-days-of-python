from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = (0,-230)

#Create the class Tartaruga
class Tartaruga(Turtle):

    #Create the turtle (shape, color, speed, etc.)
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.reset_position()
        self.setheading(90)
        self.speed("fast")

    #Method to move the turtle (just forward)
    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    #Method to reset the position of turtle
    def reset_position(self):
        self.goto(STARTING_POSITION)