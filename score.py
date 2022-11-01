from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.wrote()

    def wrote(self):
        self.write(f"Score : {self.score}", False, align='center', font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.wrote()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align='center', font=('Arial', 18, 'normal'))
