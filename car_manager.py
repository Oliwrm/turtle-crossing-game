import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed=STARTING_MOVE_DISTANCE
        self.all_cars=[]
        self.hideturtle()

    def create_car(self):
        new_car=Turtle('C:/Users/bardz/Downloads/db.gif')
        new_car.penup()
        new_car.shapesize(1,2,1)
        #new_car.color(random.choice(COLORS))
        new_car.goto(300,(random.randint(-5,5))*40)
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT


