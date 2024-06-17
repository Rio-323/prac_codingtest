import sys as s
n = int(s.stdin.readline().strip())
a = list(map(int, s.stdin.readline().strip().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))