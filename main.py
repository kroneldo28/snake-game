import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake, MOVE_DISTANCE

# Let's create a window and set it up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect food collision
    if snake.head.distance(food) < MOVE_DISTANCE:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        # game_on = False
        # scoreboard.game_over()

    # Detect tail collision
    # TODO : There's something wrong here. Play a few times to see how to fix it
    for part in snake.snake[1:]:
        if snake.head.distance(part) < MOVE_DISTANCE:
            scoreboard.reset()
            snake.reset()
            # game_on = False
            # scoreboard.game_over()

screen.exitonclick()


