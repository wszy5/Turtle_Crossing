from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.move_speed = 0
        self.goto(x=random.randrange(300, 310, 50), y=random.randrange(-250, 250, 50))




    def drive(self):
        self.goto(self.xcor()-MOVE_INCREMENT - self.move_speed, self.ycor())