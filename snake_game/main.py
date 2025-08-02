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

# Create the snake, the food and the scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Function to move the snake with keys
def bind_keys():
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

#Initiate the game
def play_game():

    #Reset the instances
    snake.reset()
    scoreboard.reset()
    food.refresh()

    #Listen the screen to move the snake with keys
    screen.listen()
    bind_keys()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()

        #Detect collision with food
        if snake.head.distance(food) < 15:
            scoreboard.increase()
            snake.extend()
            food.refresh()

        #Detect collision with wall
        if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
            game_is_on = False

        #Detect collision with tail
        for segment in snake.squares[1:]:
            if snake.head.distance(segment) < 0.1:
                game_is_on = False

# While loop to ask the player if he wants to continue playing or finish the game
while True:
    play_game()
    answer = screen.textinput("GAME OVER", "Play again (y/n)? ").lower()
    if answer != "y":
        break

screen.bye()
