from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
goal = vector(0, -10)
score= 0

def change(x, y):
    "The direction of the snake is changed."
    goal.x = x
    goal.y = y

def inside(head):
    "Return true is head is inside the boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move the snake forward of one step."
    global score
    head = snake[-1].copy()
    head.move(goal)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'black')
        update()
        penup()
        goto(0, 0)
        color("Red")
        write("GAME OVER!", align="center", font=("poppins", 24, "bold"))
        return 

    snake.append(head)

    if head == food:
        score+=1
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'yellow')

    square(food.x, food.y, 9, 'Red')
    penup()
    goto(-190, 180)  # Position the score at the top left corner
    color("black")
    write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
bgpic("snakegame.gif")
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()