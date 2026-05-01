from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}     High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def load_high_score(self):
        try:
            with open("data.txt") as data:
                value = data.read().strip()
                return int(value) if value else 0
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

    def save_game_record(self):
        with open("record.txt", mode="a") as record:
            record.write(f"\n{self.player_name} : {self.score}")

    def reset(self):
        if self.score > 0:
            self.save_game_record()

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()


        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        #self.clear()
        #self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()