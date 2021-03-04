from turtle import Turtle, Screen
import random
import turtle
pet = Turtle()
pet.shape("turtle")
pet.shapesize(2)
pet.color("blue")
pet.speed(5)

job = Turtle()
job.shape("turtle")
job.shapesize(2)
job.color("red")
job.speed(3)



turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)
    return color_tuple


directions = [0, 90, 180, 270]
rounds = 0
while rounds < 1000:
    rounds += 1
    pet.pensize(20)
    pet.forward(50)
    pet.setheading(random.choice(directions))
    pet.pencolor(random_color())

    job.pensize(20)
    job.forward(50)
    job.setheading(random.choice(directions))
    job.pencolor(random_color())








screen = Screen()
screen.exitonclick()

