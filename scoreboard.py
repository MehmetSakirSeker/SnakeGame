from turtle import Screen,Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}",align="center",font=("Arial",15,"normal"))

    def adding_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial", 35, "normal"))