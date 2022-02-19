from turtle import Screen
from assets import Paddle, Ball, BlockManager, Scoreboard
import time

GAME_SPEED = 2
# Added to keep game speed consistant as blocks disappear
# Increments by .0001 per block hit
sleep_time = 0.001
# Start with game paused
PAUSED = True


def pause_game():
    global PAUSED
    if PAUSED:
        PAUSED = False
        scoreboard.ht()
        scoreboard.clear()
        scoreboard.update_scoreboard()
    elif not PAUSED:
        PAUSED = True
        scoreboard.paused()


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
screen.onkeypress(pause_game, 'space')

game_active = True

# Call instructions at start of game
scoreboard.paused()

while game_active:
    # Pause code
    if not PAUSED:
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
            scoreboard.lives -= 1
            scoreboard.update_scoreboard()
            ball.reset_ball()

        # Detect block colision
        if ball.ycor() > 0:
            for count, block in enumerate(blockmanager.blocklist):
                if block.distance(ball) < 40:
                    block.ht()  # "Hides" the turtle
                    del blockmanager.blocklist[count]  # Deletes block object
                    ball.top_bottom_bounce()
                    scoreboard.increase_score()
                    sleep_time += 0.0001

        # Detect WIN
        if len(blockmanager.blocklist) == 0:
            scoreboard.you_win()
            game_active = False

        # Detect LOSS
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_active = False

        time.sleep(sleep_time)
        screen.update()

    elif PAUSED:
        time.sleep(.01)
        screen.update()

screen.exitonclick()
