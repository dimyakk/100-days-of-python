from turtle import Turtle
from random import choice, randint
COLORS = ["orange","yellow","red","green","blue","purple"]
MOVE_DISTANCE = 5
INCREASE_SPEED = 10

#Create the CarDealer to manage the cars
class CarDealer:

    #Attributes: cars (list for the new_cars) and speed of cars
    def __init__(self):
        self.cars = []
        self.car_speed = MOVE_DISTANCE

    #Method to create the new cars
    def create_cars(self):
        random_chance = randint (1,6)
        if random_chance == 2 or random_chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = randint(-200,200)
            new_car.goto(300,random_y)
            self.cars.append(new_car)

    #Method to move cars automatically
    def move_cars(self):
        for car in self.cars:
            car.bk(self.car_speed)

    #Method to increase the speed of cars
    def increase_speed(self):
        self.car_speed += INCREASE_SPEED
