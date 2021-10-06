#Initialize Turtle
import turtle
import random
abby = turtle.Turtle()
turtle.colormode(255)
abby.speed(500)

#Functions
def randomDot():
    for i in range(200):
        r=random.randint(0,255)
        b=random.randint(0,255)
        g=random.randint(0,255)
        c=random.randint(0,200)
        x=random.randint(-500,500)
        y=random.randint(-500,500)
        abby.penup()
        abby.goto(x,y)
        abby.pendown()
        abby.color(r,b,g)
        abby.begin_fill()
        abby.circle(c)
        abby.end_fill()
        print(r)
        print(b)
        print(g)
    

#Main
randomDot()
