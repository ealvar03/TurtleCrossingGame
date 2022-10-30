from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def is_at_top(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

