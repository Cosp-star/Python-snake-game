from snake import Snake
from time import sleep
from turtle import Screen
from pellet import Pellet
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
score = Scoreboard()
food = Pellet()
is_hit = False
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.sleft,"Left")
screen.onkey(snake.sright,"Right")

while not is_hit:
    if not food.pellet.isvisible():
        food.spawn()
    screen.update()
    sleep(0.15)
    snake.run()
    wall_hit = snake.head.xcor() >= 390 or snake.head.xcor() <= -390 or snake.head.ycor() >= 390 or snake.head.ycor() <= -390



    if snake.head.distance(food.pellet) < 15 :
        food.despawn()
        snake.grow()
        score.plus1()
        print(score.score)

    if wall_hit or snake.checkhit():
        is_hit = True
        score.gameover()



screen.exitonclick()

##### known issues

# when pressing left and down or right and down at the same time, it will cause the snake to move in the other direction, causing a game over scene.


