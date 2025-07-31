from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

#Create and set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("La Vivorita")
screen.tracer(0)

#Create the snake, the food and the scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

#Detect the keys for the motion
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


#Initiate the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase()
        snake.extend()
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.squares[1:]:
        if snake.head.distance(segment) < 0.1:
            game_is_on = False
            score.game_over()

screen.exitonclick()
