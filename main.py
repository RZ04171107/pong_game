from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

COLLISION_DIS = 15
CEILING_YCOR = 280
FLOOR_YCOR = -280
PADDLE_DIS_MAX = 50
PADDLE_HIT_XCOR_R = 320
PADDLE_HIT_XCOR_L = -320
BOUND_L = -380
BOUND_R = 380

screen = Screen()
paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with ceiling and floor
    if ball.ycor() > CEILING_YCOR or ball.ycor() < FLOOR_YCOR:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle_right) < PADDLE_DIS_MAX and ball.xcor() > PADDLE_HIT_XCOR_R or ball.distance(
            paddle_left) < PADDLE_DIS_MAX and ball.xcor() < PADDLE_HIT_XCOR_L:
        ball.bounce_x()

    # Detect paddles misses
    # If yes, reset the ball's position to the center of the screen.
    # The ball should then start moving towards the other player.
    if ball.xcor() > BOUND_R:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < BOUND_L:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
