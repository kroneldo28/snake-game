from turtle import Turtle
FONT = ("Verdana", 15, "normal")
ALIGNMENT = "center"
# FILE = "/Users/kroneldo28/Dropbox/Mon Mac (macbook-pro-de-ronel.home)/Downloads/data.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        # with open(FILE, mode="r") as file:
        #     self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
            # with open(FILE, mode="w") as file:
            #     file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)



