class Ball:
    def __init__(self):
        self.position = PVector(width * 0.5, height * 0.5)
        self.w = 20
        self.velocity = PVector(5, 5)
        self.score_player_one = False
        self.score_player_two = False

    def show(self):
        fill(255)
        ellipse(self.position.x, self.position.y, self.w, self.w)

    def move(self):
        self.position = self.position.add(self.velocity)

    def border(self):
        if self.position.x > width:
            self.velocity.x *= -1
        elif self.position.x > height:
            self.velocity.y *= -1
            self.score_player_one = True
        elif self.position.x < width:
            self.velocity.x *= -1
        elif self.position.x < height:
            self.velocity.y *= -1
            self.score_player_two = True

    def update(self):
        self.move()
        self.border()