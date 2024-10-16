import heapq

def manhattan(curr, goal):
    ans = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if goal[i][j] == curr[k][l]:
                        ans += abs(i - k) + abs(j - l)
    return ans

def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal), start))
    close_set = set()
    gscore = {}
    gscore[tuple(map(tuple, start))] = 0
    parent = {}

    while open_set:
        _, curr = heapq.heappop(open_set)
        if curr == goal:
            return path(parent, curr)
        close_set.add(tuple(map(tuple, curr)))
        for neighbour in neighbours(curr):
            if tuple(map(tuple, neighbour)) in close_set:
                continue
            new_g = gscore[tuple(map(tuple, curr))] + 1
            if tuple(map(tuple, neighbour)) not in gscore or new_g < gscore[tuple(map(tuple, neighbour))]:
                parent[tuple(map(tuple, neighbour))] = curr
                gscore[tuple(map(tuple, neighbour))] = new_g
                heapq.heappush(open_set, (new_g + manhattan(neighbour, goal), neighbour))
    return "No solution"

def neighbours(curr):
    n = []
    x, y = 0, 0
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i in range(3):
        for j in range(3):
            if curr[i][j] == 0:
                x, y = i, j
                break
    for dx, dy in directions:
        if 0 <= x + dx < 3 and 0 <= y + dy < 3:
            new_state = [row.copy() for row in curr]
            new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
            n.append(new_state)
    return n 

def path(parent, curr):
    fol = [curr]
    while tuple(map(tuple, curr)) in parent:
        curr = parent[tuple(map(tuple, curr))]
        fol.append(curr)
    return list(reversed(fol))

start = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
result = astar(start, goal)
if result != "No solution":
    for ind,state in enumerate(result):
        print(f"Step: {ind}")
        for row in state:
            print(row)
        print()
    print("Goal Reached")
else:
    print(result)
