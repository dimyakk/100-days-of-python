from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

#Create the class Scoreboard that inherits for Turtle
class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,277)
        self.color("white")
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    #Method for game over
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    #Method for increase the score
    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

