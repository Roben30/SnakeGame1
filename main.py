from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
score = Score()


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280:
        score.game_over()
        is_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            score.game_over()


screen.exitonclick()
