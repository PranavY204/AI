import heapq

class Puzzle:
    def __init__(self):
        self.board = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
        self.end = [
        [2, 8, 1],
        [0, 4, 3],
        [7, 6, 5]
    ]
    def getMoves(self, board):
        zero_pos = self.zero_index(board)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        valid_moves = []
        for move in moves:
            if 0 <= zero_pos[0] + move[0] < 3 and 0 <= zero_pos[1] + move[1] < 3:
                valid_moves.append(move)
        return valid_moves

    def zero_index(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return [i, j]
    
    def bhash(self, board):
       return tuple(map(tuple, board))
    
    def display(self, board):
        for ls in board:
            print(*ls)
            
    def manhattan_distance(self, state):
        """Calculate the total Manhattan distance of the state."""
        distance = 0
        for i in range(9):
            old = self.get_index(i, state)
            final = self.get_index(i, self.end)
            distance += (abs(final[0] - old[0]) + abs(final[1] - old[1]))
        return distance
    
    def get_index(self, el, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == el:
                    return [i, j]
    
    def misplaced(self, state):
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.end[i][j]:
                    misplaced += 1
        return misplaced 

    
    def a_star(self):
        heap = []
        heapq.heappush(heap, (self.manhattan_distance(self.board) + self.misplaced(self.board), 0, self.board, []))  # (priority, cost, current state, path)
        visited = set()  # Track visited states

        while heap:
            priority, cost, state, path = heapq.heappop(heap)

            # Convert the state to a tuple to store in a set (hashable)
            state_tuple = tuple(map(tuple, state))

            if state_tuple in visited:
                continue

            visited.add(state_tuple)

            # If the current state is the goal state, return the path
            if self.bhash(state) == self.bhash(self.end):
                for p in path + [state]:
                    self.display(p)
                    print("------")
                return

            # Get all possible moves (neighbors) and add them to the heap
            for move in self.getMoves(state):
                new_board = [row[:] for row in state]
                zeroPos = self.zero_index(new_board)
                newPos = [zeroPos[0] + move[0], zeroPos[1] + move[1]]
                new_board[newPos[0]][newPos[1]], new_board[zeroPos[0]][zeroPos[1]] = new_board[zeroPos[0]][zeroPos[1]], new_board[newPos[0]][newPos[1]]
                if tuple(map(tuple, new_board)) not in visited:
                    new_cost = cost + 1 # Each move has a cost of 1
                    priority = self.manhattan_distance(new_board) + self.misplaced(new_board)
                    heapq.heappush(heap, (priority, new_cost, new_board, path + [state]))

    
    def dfs(self):
        stack = []
        visited = []
        stack.append(self.board)
        visited.append(self.bhash(self.board))
        while stack:
            top = stack[-1]
            if self.bhash(top) == self.bhash(self.end):
                break
            valid_moves = self.getMoves(top)
            added = False
            # print(zeroPos, valid_moves)
            for move in valid_moves:
                new_board = [row[:] for row in top]
                zeroPos = self.zero_index(new_board)
                newPos = [zeroPos[0] + move[0], zeroPos[1] + move[1]]
                new_board[newPos[0]][newPos[1]], new_board[zeroPos[0]][zeroPos[1]] = new_board[zeroPos[0]][zeroPos[1]], new_board[newPos[0]][newPos[1]]
                if self.bhash(new_board) not in visited:
                    stack.append(new_board)
                    visited.append(self.bhash(new_board))
                    added = True
                    break
            if not added:
                stack.pop()
        while stack:
            self.display(stack.pop(0))
            print("--------")
    
    
c = Puzzle()
print('DFS: ')
c.dfs()
print("MD: ")
c.a_star()
# print(c.zero_index("123405678"))
            
