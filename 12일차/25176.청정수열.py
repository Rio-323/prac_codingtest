import sys as s

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(s.stdin.readline().strip())
print(factorial(n))