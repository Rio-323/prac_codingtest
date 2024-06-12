import sys as s

n1, n2, n3 = map(int, s.stdin.readline().split(':'))
cnt = 0

if n1 == 0 and n2 == 0 and n3 == 0:
    cnt += 0
else:
    for n in [n1, n2, n3]:
        if 0 < n < 13:
            if all(0 <= other < 60 for other in [n1, n2, n3] if other != n):
                cnt += 2

print(cnt)