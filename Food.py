import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.goto(random.randint(-280, 280),
                  random.randint(-280, 280))

    def being_random_position(self):
        self.goto(random.randint(-280, 280),
                  random.randint(-280, 280))
