# hanoi tornyai rekurzív megközelítéssel

n = int(input().strip())
count_steps = 0
out = []

def hanoi_solver(n, rod1, rod2, rod3):
    global count_steps
    if n == 0:
        return
    hanoi_solver(n - 1, rod1, rod3, rod2)
    out.append(f"{rod1} {rod3}")
    # print(rod1, rod3)
    count_steps += 1
    hanoi_solver(n - 1, rod2, rod1, rod3)

hanoi_solver(n, 1, 2, 3)
print(count_steps)
[print(i) for i in out]