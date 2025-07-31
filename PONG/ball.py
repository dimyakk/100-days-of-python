from turtle import Turtle

#Create the class Ball that inherits from Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 3
        self.move_y = 3
        self.move_speed = 0.04

    #Method to move the ball plus adding 3 in the X and Y coordinates, and setting with the new coordinates
    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x,new_y)

    #Method to bounce the ball when collision with the wall
    def bounce_y(self):
        self.move_y *= -1

    #Method to bounce the ball when collision with any paddle. Increased the speed of the ball
    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    #Method to reset the position and speed of the ball
    def reset_position(self,):
        self.goto(0,0)
        self.move_speed = 0.04
        self.move_ball()