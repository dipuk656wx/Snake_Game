import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scorebaord import Scoreboard



screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:

        food.refresh()
        scoreboard.clear()
        scoreboard.increase_s()
        snake.extend()



    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.clear()
        scoreboard.update_scoreboard()
        snake.reset()
    new_s = snake.segment[1:len(snake.segment)]
    for s in new_s:

        if snake.head.distance(s) < 10:
            scoreboard.clear()
            scoreboard.update_scoreboard()
            snake.reset()

































screen.exitonclick()
