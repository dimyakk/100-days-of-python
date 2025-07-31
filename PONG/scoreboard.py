from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

#Create the class Scoreboard that inherits from Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    #Method to update the score before increasing eather score
    def update_score(self):
        self.clear()
        self.goto(-100,270)
        self.write(f"{self.l_score}",align= ALIGNMENT, font = FONT)
        self.goto(100,270)
        self.write(f"{self.r_score}",align= ALIGNMENT, font = FONT)

    #Methods to increase the score for the right player or left score. Finally update the score
    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()
