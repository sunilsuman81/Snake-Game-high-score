from turtle import Turtle
import random

FOOD_X_LIMIT = 420
FOOD_Y_LIMIT = 300

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-FOOD_X_LIMIT, FOOD_X_LIMIT)
        random_y = random.randint(-FOOD_Y_LIMIT, FOOD_Y_LIMIT)
        self.goto(random_x, random_y)
