import heapq



class EightQueensAStar:

    def __init__(self, N=8):

        self.N = N  # Number of queens and size of the board (N x N)



    def is_valid(self, state, row, col):
        """
        Check if a queen can be placed at (row, col) without conflicts.
        """
        for r, c in enumerate(state):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def heuristic(self, state):
        """
        Calculate the heuristic (h) as the number of pairs of queens attacking each other.
        """
        conflicts = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(i - j) == abs(state[i] - state[j]):
                    conflicts += 1
        return conflicts

    def a_star_search(self):
        """
        A* search to solve the 8-queens problem.
        """
        # Priority queue to store nodes in format (f, g, state), where:
        # - f is the total cost (f = g + h)
        # - g is the number of queens placed so far
        # - state is a tuple representing the column positions of queens in each row up to row g
        frontier = [(0, 0, ())]
        heapq.heapify(frontier)

        while frontier:
            f, g, state = heapq.heappop(frontier)

            # Goal check: If we've placed N queens without conflicts
            if g == self.N and self.heuristic(state) == 0:
                return state  # Return the goal state as a solution

            # Generate successors by placing a queen in the next row
            for col in range(self.N):
                if self.is_valid(state, g, col):
                    new_state = state + (col,)
                    h = self.heuristic(new_state)
                    heapq.heappush(frontier, (g + 1 + h, g + 1, new_state))

        return None  # No solution found

# Initialize and solve the problem
eight_queens_solver = EightQueensAStar()
solution = eight_queens_solver.a_star_search()
print(solution)
