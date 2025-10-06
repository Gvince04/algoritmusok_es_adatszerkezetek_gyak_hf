# CSES Grid Paths I megoldás
# Megközelítés: Dinamikus Programozás
# https://cses.fi/problemset/task/1638

n = int(input())
grid = []
MOD = 10 ** 9 + 7

for i in range(n):
    grid.append([it == '.' for it in input().strip()])

dp = [[0] * n for _ in range(n)]

row = True
col = True
for i in range(n):
    if row and grid[0][i]:
        dp[0][i] = 1
    if col and grid[i][0]:
        dp[i][0] = 1

    if not grid[0][i]:
        row = False
    if not grid[i][0]:
        col = False


for i in range(1, n):
    for j in range(1, n):
        if grid[i][j]:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

print(dp[-1][-1])