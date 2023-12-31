from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
G_A = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=G_A, font=FONT)

