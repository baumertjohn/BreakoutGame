from turtle import Turtle

PADDLE_WIDTH = 7
PADDLE_HEIGHT = 1
PADDLE_SPEED = 20


class Paddle(Turtle):
    def __init__(self, y_start):
        super().__init__()
        self.y_start = y_start
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.color('blue')
        self.penup()
        self.goto(0, self.y_start)
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH, None)

    def paddle_left(self):
        x_position = self.xcor()
        y_position = self.ycor()
        if x_position > -330:
            self.goto(x_position - PADDLE_SPEED, y_position)

    def paddle_right(self):
        x_position = self.xcor()
        y_position = self.ycor()
        if x_position < 330:
            self.goto(x_position + PADDLE_SPEED, y_position)


class Ball(Turtle):
    def __init__(self, ball_speed=0.1):
        super().__init__()
        self.ball_speed = ball_speed
        self.create_ball()

    def create_ball(self):
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.ball_x_travel = self.ball_speed
        self.ball_y_travel = self.ball_speed

    def move_ball(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + self.ball_x_travel,
                  current_y + self.ball_y_travel)

    def side_bounce(self):
        self.ball_x_travel *= -1

    def top_bottom_bounce(self):
        self.ball_y_travel *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.top_bottom_bounce()


class Block(Turtle):
    def __init__(self):
        super().__init__()
