from random import randint
from turtle import Turtle


class  Pellet():

    def __init__(self):
        self.pellet = Turtle("circle")
        self.pellet.shapesize(0.5,0.5)
        self.pellet.penup()
        self.pellet.color("red")
        self.pellet.hideturtle()





    def spawn(self):
        self.pellet.showturtle()
        maprange = randint(-350,380)
        self.pellet.goto(maprange,maprange)

    def despawn(self):
        self.pellet.hideturtle()







