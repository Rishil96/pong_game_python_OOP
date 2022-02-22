from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_score += 1

    def right_point(self):
        self.right_score += 1

    def winner(self, winner):
        self.goto(0, 100)
        self.write(winner, align=ALIGNMENT, font=("Courier", 40, "normal"))
