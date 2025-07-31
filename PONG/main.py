from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Create the screen:
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    

#Create and move the paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

#Create the ball and scoreboard
ball = Ball()
scoreboard = Scoreboard()

#Initiate the game
game_is_on = True
while game_is_on:
    screen.update() #Update the screen
    ball.move_ball() #The ball moves
    time.sleep(ball.move_speed) #Ball speed

    #Collision for the walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision for the right paddle and bounce
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.setx(320) #Set the ball to x = 320 so that it doesn't bounce too many times with the paddle right.
        ball.bounce_x()

    #Collision for the right paddle and bounce
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.setx(-320) #Set the ball to x = -320 so that ir doesn't bounce too many times with the paddle left.
        ball.bounce_x()

    #Collision for the right wall and increase the score for the left player. Reset the position for the ball.
    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    #Collision for the left wall and increase the score for the right player. Reset the position for the ball.
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()