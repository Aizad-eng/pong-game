from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.display_score()

    def increment_score(self):
        self.score +=1
        print(self.score)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='left', font=('Arial', 15, 'normal'))