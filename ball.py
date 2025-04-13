from turtle import Turtle


class Ball(Turtle):

    def __init__(self, shape="circle"):
        super().__init__(shape)
        self.color("white")
        self.penup()
        self.speeding = 0.01
        self.x_move = 2
        self.y_move = 2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.speeding *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speeding = 0.01
        self.x_move *= -1
