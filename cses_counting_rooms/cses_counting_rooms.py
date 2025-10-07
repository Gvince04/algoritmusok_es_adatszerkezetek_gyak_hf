# CSES Counting Rooms
# Megközelítés: Gráf algoritmusok, BFS
# https://cses.fi/problemset/task/1192/

from collections import deque

n, m = [int(i) for i in input().strip().split()]
grid = [[-1 if i == "#" else 0 for i in input().strip()] for _ in range(n)]

rooms = 0
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# def print_grid():
#     global grid
#     for r in grid:
#         for i in r:
#             print(f"{('#' if i == -1 else i):>3}", end="")
#         print()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            rooms += 1
            s = deque([(i, j)])
            grid[i][j] = rooms
            while s:
                x, y = s.popleft()
                for dir in directions:
                    nx, ny = x + dir[0], y + dir[1]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if grid[nx][ny] == 0:
                        s.append((nx, ny))
                        grid[nx][ny] = rooms

# print_grid()

print(rooms)
