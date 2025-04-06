from turtle import Turtle, Screen
import random

screen = Screen()
jose_turtle = Turtle()
jose_turtle.hideturtle()
jose_turtle.speed("fastest")
jose_turtle.penup()
screen.colormode(255)
jose_turtle.pensize(10)
jose_turtle.setheading(225)
jose_turtle.forward(300)
jose_turtle.setheading(0)
dots = 100

for dot_c in range(1, dots + 1):
    jose_turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    jose_turtle.dot(20)
    jose_turtle.forward(50)
    
    if dot_c % 10 == 0:
        jose_turtle.setheading(90)
        jose_turtle.forward(50)
        jose_turtle.setheading(180)
        jose_turtle.forward(500)
        jose_turtle.setheading(0)
        
screen.exitonclick()
