from turtle import Turtle
FONT = ("Courier",20,"normal")
ALIGNMENT = "left"

#Create the class ScoreBoard
class Scoreboard(Turtle):

    #Create de scoreboard (color, level, etc.)
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_level()

    #Method to update the level of game: clear, position and re-write.
    def update_level(self):
        self.clear()
        self.goto(-250,250)
        self.write(f"Level :{self.level}",align=ALIGNMENT,font=FONT)

    #Method to increase the level: first increase and then update
    def increase_level(self):
        self.level += 1
        self.update_level()

    #Method to game over: new position (0,0) and write GAME OVER
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
