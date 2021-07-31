import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
screen.listen()
screen.onkey(player.go, "Up")

cars = []
step = 0

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    step += 1
    if step % 6 == 0:
        car = CarManager()
        cars.append(car)
        for car in cars:
            car.drive()
            if car.distance(player) < 20:
                scoreboard.game_over()
                time.sleep(2)
                game_is_on = False
    if player.ycor() == 290:
        player.next()
        scoreboard.new_level()
        for car in cars:
            car.move_speed += 3

    screen.update()

screen.exitonclick()
