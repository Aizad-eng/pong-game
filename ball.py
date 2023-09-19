import time
from turtle import Turtle
from scorecard import ScoreCard

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.MOVE_X = 10
        self.MOVE_Y = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x + self.MOVE_X, new_y + self.MOVE_Y)
        if self.collided_with_top_wall():
            self.reverse_y_direction()

    def collided_with_right_wall(self):
        if self.xcor()>=400:
            return True

    def collided_with_left_wall(self):
        if self.xcor()<=-400:
            return True

    def reverse_x_direction(self):
        self.MOVE_X *= -1
        self.move_speed*=0.9
    def reverse_y_direction(self):
        self.MOVE_Y *= -1
    def collided_with_top_wall(self):
        if self.ycor()>=300 or self.ycor()<=-300:
            return True

    def increase_speed(self):
        time.sleep()
    def refresh(self):
        self.move_speed = 0.1
        self.goto(0,0)