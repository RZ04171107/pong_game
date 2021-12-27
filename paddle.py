from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, init_ycor):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(init_ycor, 0)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def paddle_down(self):
        self.sety(self.ycor() - 20)
