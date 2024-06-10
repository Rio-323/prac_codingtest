from heapq import heappush, heappop
import sys as s

n = int(s.stdin.readline().strip())
heap = []
results = []

for _ in range(n):
    x = int(s.stdin.readline().strip())
    if x:
        heappush(heap, x) # x가 0이 아닌 경우 힙에 추가
    else: # x가 0인 경우
        if heap: # 힙이 비어 있지 않다면 최솟값을 결과에 추가
            results.append(heappop(heap))
        else: # 힙이 비어 있다면 결과에 0을 추가
            results.append(0)

print('\n'.join(map(str, results)))

# 결과 예측
# heap = 12345678 1 2 0
#
# results = 0 1 2 12345678 0
