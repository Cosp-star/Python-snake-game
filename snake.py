from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.sq = 3
        self.bodylist = []
        self.first_move = True
        for i in range(3):
            self.body = Turtle(shape="square")
            self.body.penup()
            self.body.color("lime")
            self.body.goto(x=i * 20, y=0)
            self.bodylist.append(self.body)
        self.head = self.bodylist[0]

    def run(self):
        for i in range(len(self.bodylist) - 1, 0, -1):
            newx = self.bodylist[i - 1].xcor()
            newy = self.bodylist[i - 1].ycor()
            self.bodylist[i].goto(newx, newy)
        self.head.forward(20)

    def grow(self):
        self.sq += 1
        self.body = Turtle(shape="square")
        self.body.penup()
        self.body.color("lime")
        self.body.goto(x=self.bodylist[-1].xcor(), y=self.bodylist[-1].ycor())
        self.bodylist.append(self.body)

    def up(self):
        heading = self.head.heading()

        if heading == 90 or heading == 270:
            pass
        elif heading == 0:
            self.head.left(90)
        elif heading == 180:
            self.head.right(90)
        else:
            self.head.left(180)

    def down(self):
        heading = self.head.heading()

        if heading == 90 or heading == 270:
            pass
        elif heading == 0:
            self.head.left(270)
        elif heading == 180:
            self.head.left(90)

    def sleft(self):
        heading = self.head.heading()

        if heading == 0 or heading == 180:
            pass
        elif heading == 90:
            self.head.left(90)
        else:
            self.head.left(270)

    def sright(self):
        heading = self.head.heading()
        if heading == 0 or heading == 180:
            pass
        elif heading == 270:
            self.head.left(90)
        else:
            self.head.left(270)

    def checkhit(self):             # I had an issue where the checkhit() method always outputs true when the snake moves for the first time, still havent found a solution for it so i added a temporary solution, it will work but will increase redundancy

        if not self.first_move:
            for body in self.bodylist[1:]:
                if self.head.distance(body) < 10:
                    return True
            return False
        else:
            self.first_move = False
            return False

