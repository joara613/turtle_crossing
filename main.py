import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    # create random car
    car_manager.create_random_car()

    # Detect successful crossing
    if player.ycor() > 280:
        scoreboard.level_up()
        player.go_to_start()
        car_manager.car_speed_up()

    # Collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.show_game_over()
            print(player.distance(car))


screen.exitonclick()