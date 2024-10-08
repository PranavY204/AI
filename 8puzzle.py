import copy
class Puzzle:
    def __init__(self):
        self.board = [[2, 1, 3], [5, 7, 8], [0, 4, 6]]
        self.end = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.dfs()
    def getMoves(self, board):
        zero_pos = self.zero_index(board)
        valid_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for move in valid_moves:
            if 0 <= zero_pos[0] + move[0] < 3 and 0 <= zero_pos[1] + move[1] < 3:
                continue
            else:
                valid_moves.remove(move)
        return valid_moves

    def zero_index(self, board):
        idx = self.hash(board).find("0")+1
        return [idx//3, idx%3]
    
    def hash(self, board):
        res = ""
        for i in range(3):
            for j in range(3):
                res += str(self.board[i][j])
        return res
    def display(self, board):
        for ls in board:
            print(*ls)
    
    def dfs(self):
        stack = []
        visited = []
        stack.append(self.board)
        visited.append(self.hash(self.board))
        top = stack.pop()
        while top != self.end:
            valid_moves = self.getMoves(top)
            added = False
            for move in valid_moves:
                new_board = top.copy()
                zeroPos = self.zero_index(top)
                print(zeroPos, move)
                new_board[zeroPos[0] + move[0]][zeroPos[1] + move[1]], new_board[zeroPos[0]][zeroPos[1]] = new_board[zeroPos[0]][zeroPos[1]], new_board[zeroPos[0] + move[0]][zeroPos[1] + move[1]]
                if self.hash(new_board) not in visited:
                    stack.append(new_board)
                    visited.append(self.hash(new_board))
                    added = True
                    break
            if not added:
                stack.pop()
            top = stack.pop()
        while stack:
            self.display(stack.pop())
    
    
c = Puzzle()
# print(c.zero_index("123405678"))
            
