import time
from turtle import Turtle, Screen
from paddle  import Paddle
from ball import Ball
from scorecard import ScoreCard

screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
r_scorecard = ScoreCard((250, 250))
l_scorecard = ScoreCard((-250, 250))

screen.update()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    ball.move_ball()
    screen.update()
    time.sleep(ball.move_speed)

    if ball.collided_with_right_wall():
        l_scorecard.increment_score()
        ball.reverse_x_direction()
        ball.refresh()
    elif ball.collided_with_left_wall():
        r_scorecard.increment_score()
        ball.reverse_x_direction()
        ball.refresh()

    if r_paddle.distance(ball)<=50 and ball.xcor()>320 or l_paddle.distance(ball) <= 50 and ball.xcor()<-320:
        ball.reverse_x_direction()

    if r_scorecard.score>=3:
        print("Right Paddle Won!")
        is_game_on = False
    elif l_scorecard.score>=3:
        print("Left paddle won!")
        is_game_on = False


screen.exitonclick()


