import math
import random
def cost(x):
    return math.sin(x)

def hill_climbing(initial_sol=0, steps=0.01, max_steps=1000):
    print(f"Initial sol: {initial_sol}; steps: {steps}")
    current = initial_sol
    best = current
    for _ in range(max_steps):
        neighbor = [current + steps, current - steps]
        # print(neighbor)
        neighbor.sort(key=lambda x : cost(x))
        current = neighbor[-1]
        if cost(best) < cost(current):
            best = current
        else:
            break 
        print(f"Current: {current}, Best: {best}")
    return best
initial_sol = random.uniform(-10, 10)
steps = random.choice((00.01, 0.001))
print(hill_climbing(initial_sol, steps))
