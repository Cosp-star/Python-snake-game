from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,360)
        self.color("white")
        self.write(f"score: {self.score}", align="center", font=("Yu Gothic Light", 25,"normal"))
        self.hideturtle()
    def plus1(self):
        self.score+=1
        self.reset()
        self.goto(0, 360)
        self.color("white")
        self.write(f"score: {self.score}", align="center", font=("Yu Gothic Light", 25, "normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.color("white")
        self.write("Game Over!", align="center", font=("Yu Gothic Light", 25, "normal"))