from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

#Create the class Paddle that inherits from Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    #Methods to move the paddles up or down
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE #Create a Y coordinate: the position for the paddle plus the MOVE_DISTANCE
        self.goto(self.xcor(),new_y) #Setting the paddle with the new Y coordinate

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

