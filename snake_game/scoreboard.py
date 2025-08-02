from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

#Create the class Scoreboard that inherits for Turtle
class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,277)
        self.color("white")
        self.update_scoreboard()

    #Method to update the scoreboard (update the score and high score)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    #Method to reset the scoreboard: if there is a new high score, it replaces it and set the score to 0
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    #Method for increase the score
    def increase(self):
        self.score += 1
        self.update_scoreboard()

