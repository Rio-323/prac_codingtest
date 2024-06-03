import sys as s
a, b = map(str, s.stdin.readline().split())
b = int(b)

num = int(a, b) # 10진법으로 변환해주는 방법
print(num)