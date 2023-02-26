FONT = ("Courier", 24, "normal")
PRAISE=["ROCK ON !","YOU GO GIRLIE!","NGHHH UR SO GOOD","BET U CANT DO THIS","OK ILL SHUT UP"]
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-250,250)
        self.write(self.score,align="left",font=FONT)
    def point(self):
        self.score+=1
        self.update_score()
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER \n FINAL SCORE: {self.score}",align="center",font=("Courier",40,"bold"))

    def praise(self):
        self.goto(0,0)
        self.write(PRAISE[self.score],align="center",font=("Courier",40,"bold"))

