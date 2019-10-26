class Player:
    def __init__(self, w, h):
        self.position = PVector(w, h)
        self.w = 200
        self.h = 20

    def show(self):
        fill(255)
        rect(self.position.x, self.position.y, self.w, self.h)

    def move(self, dir):
        if dir == "left":
            self.position.x -= 10
        elif dir == "right":
            self.position.x += 10

    def check_collision(self, other):
        first_check = other.position.x >= self.position.x and other.position.x < self.position.x + self.w
        second_check = other.position.y + other.w > self.position.y and other.position.y < self.position.y + self.h
        if first_check and second_check:
            return True
