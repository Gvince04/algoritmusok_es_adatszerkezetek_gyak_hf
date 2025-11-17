# Bitmaszkolás, részhalmaz keresés, brute force

import sys

n = sys.stdin.readline()
n = int(n)
weights = sys.stdin.readline()
weights = list(map(int, weights.split()))

total_sum = sum(weights)
min_diff = float('inf')

for i in range(1 << n):
    subset_sum = 0
    for j in range(n):
        if (i >> j) & 1:
            subset_sum += weights[j]
        
    other_sum = total_sum - subset_sum
    
    min_diff = min(min_diff, abs(subset_sum - other_sum))
    
print(min_diff)