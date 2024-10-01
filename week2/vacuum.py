import random
class Cleaner:
    def __init__(self):
        self.env = [None, None]
        for i in range(2):
            self.env[i] = random.choice(("C", "D"))
        self.pos = 0
        self.pseq = []
        self.clean()

    def display(self):
        print("Current percept seq: ", self.pseq)
        print("Current env: ", self.env)

    def clean(self):
        while True:
            self.display()
            self.pseq.append((self.pos, self.env[self.pos]))
            if self.env[self.pos] == "D":
                print(f"Room {self.pos} is dirty, cleaning...")
                self.env[self.pos] = "C"
            else:
                print("Room is clean...")
                if self.pos == 1:
                    print("Moving left...")
                else:
                    print("Moving right...")
            self.display()
            self.env[self.pos] = random.choice(("C", "D"))
            self.pos = (self.pos + 1)%2

c = Cleaner()
