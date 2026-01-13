from turtle import Turtle, Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key= "Up")
screen.onkey(snake.down, key= "Down")
screen.onkey(snake.left, key= "Left")
screen.onkey(snake.right, key= "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:   #Eat food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()
        # # scoreboard.game_over()
        # is_game_on = False

    #Hit the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

            # scoreboard.game_over()
            # is_game_on = False




screen.exitonclick()