import sys as s

def max_late(t):
    factors = [i for i in range(101) if t >= i + (i ** 2)]
    return max(factors) if factors else None

n = int(s.stdin.readline().strip())
late = [int(s.stdin.readline().strip()) for _ in range(n)]
result = [max_late(i) for i in late]

print('\n'.join(map(str, result)))