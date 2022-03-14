from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.length = len(self.snake)
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(STARTING_POSITION[i])
            self.snake.append(turtle)

    def move(self):
        for part in range(self.length - 1, 0, -1):
            new_pos = self.snake[part - 1].pos()
            self.snake[part].setpos(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
