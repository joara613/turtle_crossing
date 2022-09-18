from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.starting_cars = 15
        self.move_speed = STARTING_MOVE_DISTANCE
        for num in range(self.starting_cars):
            x_position = random.randint(-280, 280)
            self.create_car(x_position)

    def create_car(self, x_position):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        car.goto(x_position, random_y)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def create_random_car(self):
        if random.randint(0, 5) == 1:
            self.create_car(300)

    def car_speed_up(self):
        self.move_speed += MOVE_INCREMENT
