import sys

n = int(sys.stdin.readline().strip())
archer = list(map(int, sys.stdin.readline().strip().split()))

high, count, max_count = 0, 0, 0

for i in archer:
    if i > high:
        high = i
        count = 0
    else:
        count += 1
        max_count = max(max_count, count)

print(max_count)