from turtle import Screen
from snake import  Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
WALL_X_LIMIT = 430
WALL_Y_LIMIT = 330

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

COLOR_OPTIONS = {"yellow", "green", "blue", "red", "white", "purple", "orange", "pink", "cyan"}

player_name = screen.textinput("Player Name", "Enter your name before starting:")
if not player_name or not player_name.strip():
    player_name = "Player"
else:
    player_name = player_name.strip()

snake_color = screen.textinput(
    "Snake Color",
    "Choose snake color (yellow, green, blue, red, white, purple, orange, pink, cyan):",
)
if not snake_color or not snake_color.strip():
    snake_color = "yellow"
else:
    snake_color = snake_color.strip().lower()
    if snake_color not in COLOR_OPTIONS:
        snake_color = "yellow"

snake = Snake(snake_color)
food = Food()
scoreboard = Scoreboard(player_name)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if (
        snake.head.xcor() > WALL_X_LIMIT
        or snake.head.xcor() < -WALL_X_LIMIT
        or snake.head.ycor() > WALL_Y_LIMIT
        or snake.head.ycor() < -WALL_Y_LIMIT
    ):
        #game_is_one = False
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            #game_is_one = False
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

    #if head collides with any segment in the tail





screen.exitonclick()