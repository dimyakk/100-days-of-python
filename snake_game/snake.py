from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

#Create the class Snake that inherits for Turtle
class Snake:
    def __init__(self):
        self.squares = [] #Attribute that creates a list where each segment of the snake is saved
        self.create_snake() #Call the method to create the snake
        self.head = self.squares[0] #Attribute that sets the first square as the first element

    #Method to create the snake (positions have 3 elements), so the snake starts with 3 squares
    def create_snake(self):
        for position in POSITIONS:
            self.add_square(position)

    #Method to add a new square to the list [squares]
    def add_square(self,position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    #Method to extend the snake
    def extend(self):
        self.add_square(self.squares[-1].position()) #The position for the new square is the position of the last square

    #Method to move the snake
    def move_snake(self):
        #for loop that goes from the range of the last element of the squares list (the snake) to the second to last,
        #with step -1. This is done to go through the list from back to front.
        for square_num in range(len(self.squares) - 1, 0, -1):

            #Setting the new coordinates that will be the position of the previous square
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE) #Move the head

    #Method to reset the snake when game over
    def reset(self):
        for segment in self.squares:
            segment.clear()
            segment.hideturtle()
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    #Methods to directing the snake
    #Each method will have a condition: if the heading (the direction of the snake's head) is different from the
    #opposite direction to where we want to go, the movement occurs. This prevents the snake from reversing.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
