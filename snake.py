from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.head.shape("turtle")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_part(position)

    def add_part(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.snake.append(turtle)

    def extend(self):
        self.add_part(self.snake[-1].pos())

    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
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
