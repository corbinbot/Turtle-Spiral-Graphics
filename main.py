import turtle
from turtle import Turtle, Screen, Shape
import colorgram
import random
puji = Turtle()
puji.shape("turtle")
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(60):

    puji.color(random_color())
    puji.circle(100)
    puji.left(10)


# for i in range(200):
#     puji.color(random.choice(colors))
#     puji.setheading(random.choice(directions))
#     puji.forward(40)
#     count += 1



screen = Screen()
screen.exitonclick()