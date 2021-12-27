from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

COLLISION_DIS = 15
CEILING_YCOR = 280
FLOOR_YCOR = -280
PADDLE_DIS_MAX = 50
PADDLE_HIT_XCOR_R = 320
PADDLE_HIT_XCOR_L = -320

screen = Screen()
paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()

screen.title('My Pong Game')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(paddle_right.paddle_up, 'Up')
screen.onkey(paddle_right.paddle_down, 'Down')
screen.onkey(paddle_left.paddle_up, 'w')
screen.onkey(paddle_left.paddle_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with ceiling and floor
    if ball.ycor() > CEILING_YCOR or ball.ycor() < FLOOR_YCOR:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle_right) < PADDLE_DIS_MAX and ball.xcor() > PADDLE_HIT_XCOR_R or ball.distance(paddle_left) and ball.xcor() < PADDLE_HIT_XCOR_L:
        ball.bounce_x()


screen.exitonclick()
