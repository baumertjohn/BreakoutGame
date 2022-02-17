from turtle import Turtle

PADDLE_WIDTH = 7
PADDLE_HEIGHT = 1
PADDLE_SPEED = 50

SB_FONT = ('Courier', 24, 'bold')


########## Paddle ##########
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.color('blue')
        self.penup()
        self.goto(0, -270)
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


########## Ball ##########
class Ball(Turtle):
    def __init__(self, ball_speed=2):
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
        self.goto(0, -200)
        self.top_bottom_bounce()


########## Block ##########
class BlockManager():
    def __init__(self):
        # super().__init__()
        self.blocklist = []
        self.start_game()

    def create_block(self, x_pos, y_pos, color):
        block = Turtle(shape='square')
        block.shapesize(1, 3, 1)
        block.penup()
        block.color(color)
        block.goto(x_pos, y_pos)
        self.blocklist.append(block)

    def start_game(self):
        block_colors = ['red', 'orange', 'yellow', 'green', 'blue']
        y_pos = 225
        for color in range(5):
            x_pos = -360
            for _ in range(11):
                self.create_block(x_pos, y_pos, block_colors[color])
                x_pos += 71
            y_pos -= 35

    def extra_block(self):
        # Hack to keep the game speed consistent
        block = Turtle(shape='square')
        block.shapesize(1, 3, 1)
        block.penup()
        block.color('black')
        block.goto(1000, 1000)
        self.blocklist.append(block)


########## Scoreboard ##########
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(f'SCORE: {self.score}', align='center', font=SB_FONT)

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=SB_FONT)
