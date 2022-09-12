from turtle import Turtle
FONT = ("Courier", 48, "bold")
SMALLFONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 200)
        self.color("white")
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

    def increase_score(self):

        self.clear()
        self.level +=1
        self.update_scoreboard()

    def update_scoreboard(self):

        self.write(f"level:{self.level}", move=False, align="center", font=SMALLFONT)
