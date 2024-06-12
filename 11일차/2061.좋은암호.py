import sys as s

def is_prime(k, l):
    for i in range(2, l):
        if k % i == 0:
            return 'BAD', i
    return 'GOOD', None

k, l = map(int, s.stdin.readline().split())
result, num = is_prime(k, l)

print(result if result == 'GOOD' else f"{result} {num}")
