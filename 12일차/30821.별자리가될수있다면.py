import sys as s
from itertools import combinations

n = int(s.stdin.readline().strip())
numbers = list(range(1, n + 1))
count = sum(1 for _ in combinations(numbers, 5))

print(count)