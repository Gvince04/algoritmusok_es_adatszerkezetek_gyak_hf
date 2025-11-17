n = int(input().strip())
places = [0] * n
nums = [int(i) for i in input().strip().split(" ")]

for i in range(n):
    places[nums[i] - 1] = i

rounds = 1
for i in range(1, n):
    if places[i] < places[i - 1]:
        rounds += 1

print(rounds)