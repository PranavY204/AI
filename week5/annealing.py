import random
import math

class Annealing:
    def __init__(self) -> None:
        self.initial_sol = random.uniform(-10, 10)
        self.temp = 10
        self.cooling = 0.99
        self.final = 0.01
        self.annealing()
    def cost(self, x):
        # return x**2
        return x**4 + 5*math.sin(5*math.pi*x)
    def getNeighbors(self, sol):
        return sol + random.uniform(-1, 1)
    def annealing(self):
        current = self.initial_sol
        new = current
        best = current
        while self.temp > self.final:
            new = self.getNeighbors(current)
            dE = self.cost(new) - self.cost(current)
            print(f"Temp diff: {((self.temp - self.final)*100)/self.temp:.2f}%; Current sol: {current}; New sol: {new}; Best: {best}")
            if dE < 0 or random.random() < math.exp(-dE/self.temp):
                current = new
            if self.cost(new) < self.cost(best):
                best = new
            self.temp *= self.cooling
        print(f"Final solution: {best}")

c = Annealing()
