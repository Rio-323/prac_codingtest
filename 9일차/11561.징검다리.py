# n = 1 + 2 + 3 + 4 + ... 이런식으로 1부터 k까지 합을 만족하는 것 그때의 k구하기
# k(k+1)/2 <= N -> 공식을 만족하는 것중 최대값 -> 근의 공식으로 k2 + k - 2N <= 0 (-1 + 루트 1 + - 8N) / 2

import math
import sys as s

def max_k(N):
    return int((-1 + math.sqrt(1 + (8 * N))) // 2)

num = int(s.stdin.readline().strip())
result = []

for i in range(num):
    result.append(int(s.stdin.readline().strip()))

for i in result:
    print(max_k(i))
