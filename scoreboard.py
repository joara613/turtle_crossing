from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_level()

    def level_up(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)
        
    def show_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=FONT)
        
