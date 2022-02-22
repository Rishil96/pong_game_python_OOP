from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LENGTH = 1


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto((self.xcor(), new_y))

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto((self.xcor(), new_y))
