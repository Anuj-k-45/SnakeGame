from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.write(f"Score : {self.score} High Score : {self.high_score}",align="center",font=("Courier",18,"normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}",align="center",font=("Courier",18,"normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=("Courier",18,"normal"))

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
        