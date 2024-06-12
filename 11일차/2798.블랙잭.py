import sys as s
import itertools

n, m = map(int, s.stdin.readline().split())
blackjack = list(map(int, s.stdin.readline().split()))
result = []

for combination in itertools.combinations(blackjack, 3):
    if sum(combination) <= m:
        result.append(sum(combination))

print(max(result))