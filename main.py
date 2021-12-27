from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
paddle_right = Paddle(350)
paddle_left = Paddle(-350)

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
    screen.update()

screen.exitonclick()
