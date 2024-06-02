import sys as s
a = int(s.stdin.readline().strip())

def fib(a):
    if a == 1 or a == 2:
        return 1
    else:
        return fib(a-1) + fib(a-2)

def fibonacci(a):
    return a - 2

print(fib(a), fibonacci(a))

# 그냥 피보나치를 구현하면 되는 문제 였음 return a - 2를 한 이유는 횟수는 a - 2번 실행됨.