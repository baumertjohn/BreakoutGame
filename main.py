from turtle import Screen
from assets import Paddle, Ball, Block

GAME_SPEED = 0.15

# Game screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('BREAKOUT')
screen.tracer(0)  # Reduce flicker

paddle = Paddle(-270)
ball = Ball(GAME_SPEED)

screen.listen()
screen.onkeypress(paddle.paddle_left, 'Left')
screen.onkeypress(paddle.paddle_right, 'Right')

game_active = True

while game_active:
    screen.update()

    # Move ball
    ball.move_ball()

    # Detect side wall
    if ball.xcor() < -390 or ball.xcor() > 390:
        ball.side_bounce()

    # Detect top collision
    if ball.ycor() > 290:
        ball.top_bottom_bounce()

    # Detect paddle collision
    if ball.distance(paddle) < 50 and ball.ycor() > -280:
        ball.top_bottom_bounce()

    # Detect paddle miss
    if ball.ycor() < -300:
        ball.reset_ball()

screen.exitonclick()
