from turtle import Screen
from assets import Paddle, Ball, BlockManager, Scoreboard

GAME_SPEED = 1.5

# Game screen setup
screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor('black')
screen.title('BREAKOUT')
screen.tracer(0)  # Reduce flicker

paddle = Paddle()
ball = Ball(GAME_SPEED)
blockmanager = BlockManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.paddle_left, 'Left')
screen.onkeypress(paddle.paddle_right, 'Right')

game_active = True

while game_active:
    # Move ball
    ball.move_ball()

    # Detect side wall
    if ball.xcor() < -390 or ball.xcor() > 390:
        ball.side_bounce()

    # Detect top collision
    if ball.ycor() > 290:
        ball.top_bottom_bounce()

    # Detect paddle collision
    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.top_bottom_bounce()

    # Detect paddle miss
    if ball.ycor() < -300:
        ball.reset_ball()

    # Detect block colision
    if ball.ycor() > 0:
        for count, block in enumerate(blockmanager.blocklist):
            if block.distance(ball) < 40:
                block.ht()  # "Hides" the turtle
                del blockmanager.blocklist[count]  # Deletes block object
                blockmanager.extra_block()
                ball.top_bottom_bounce()
                scoreboard.increase_score()
                
    screen.update()

screen.exitonclick()
