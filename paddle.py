from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, shape="square"):
        super().__init__(shape)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def init_position(self, x_position, y_position=0):
        self.penup()
        self.goto(x_position, y_position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
