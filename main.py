import time
from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard

screen = Screen()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
food.being_random_position()

snake = Snake()
screen.listen()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.being_random_position()
        scoreboard.adding_score()
        snake.add_tail()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()

    if (snake.head.xcor() > 285 or snake.head.xcor() < -285) or (snake.head.ycor() > 285 or snake.head.ycor() < -285):
        scoreboard.reset()
        snake.reset()


screen.exitonclick()
