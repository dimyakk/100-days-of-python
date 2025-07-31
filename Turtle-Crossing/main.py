from turtle import Screen
from tartaruga import Tartaruga
from car_dealer import CarDealer
from scoreboard import Scoreboard
import time

#Create screen and setup
screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

#Create turtle, car_dealer and scoreboard
t = Tartaruga()
car_dealer = CarDealer()
scoreboard = Scoreboard()

#Move forward
screen.listen()
screen.onkey(t.move_forward,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Create and move the cars
    car_dealer.create_cars()
    car_dealer.move_cars()

    #Detect collision between the turtle and any car
    for car in car_dealer.cars:
        if abs(t.xcor() - car.xcor()) < 25 and abs(t.ycor() - car.ycor()) < 15:
            game_is_on = False
            scoreboard.game_over()

    if t.ycor() > 210:
        scoreboard.increase_level()
        t.reset_position()
        car_dealer.increase_speed()

screen.exitonclick()