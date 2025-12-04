n, m = [int(i) for i in input().split()]



nums = [0] + [int(i) for i in input().split()]
places = [0] * (n + 1)

for i in range(1, n + 1):
	places[nums[i]] = i
	
	
rounds = 1

for i in range(1, n):
	if places[i + 1] < places[i]:
		rounds += 1
		
for _ in range(m):
	r1, r2 = [int(i) for i in input().split()]
	
	v1 = nums[r1]
	v2 = nums[r2]
	
	pairs_to_check = set()
	
	if v1 > 1: pairs_to_check.add((v1 - 1, v1))
	if v1 < n: pairs_to_check.add((v1, v1 + 1))
	if v2 > 1: pairs_to_check.add((v2 - 1, v2))
	if v2 < n: pairs_to_check.add((v2, v2 + 1))
	
	for l, h in pairs_to_check:
		if places[h] < places[l]:
			rounds -= 1
	
	nums[r1], nums[r2] = nums[r2], nums[r1]
	places[v1] = r2
	places[v2] = r1
	
	for l, h in pairs_to_check:
		if places[h] < places[l]:
			rounds += 1
			
	print(rounds)
