import random
class Cleaner:
    def __init__(self):
        self.env = [[None, None], [None, None]]
        for i in range(2):
            for j in range(2):
                self.env[i][j] = random.choice(("C", "D"))
        self.pos = [0, 0]
        self.pseq = []
        self.clean()

    def display(self):
        print("Current percept seq: ", self.pseq)
        print("Current env: ")
        print(self.env[0], self.env[1], sep="\n")

    def clean(self):
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        next_move_idx = 0
        while True:
            self.pseq.append((self.pos, self.env[self.pos[0]][self.pos[1]]))
            if self.env[self.pos[0]][self.pos[1]] == "D":
                print(f"Room {self.pos} is dirty, cleaning...")
            else:
                print("Room is clean...")
                print("Moving...")
            self.env[self.pos[0]][self.pos[1]]= random.choice(("C", "D"))
            self.pos = [self.pos[0] + moves[next_move_idx][0], self.pos[1] + moves[next_move_idx][1]]
            next_move_idx = (next_move_idx + 1)%len(moves)
            self.display()
c = Cleaner()
