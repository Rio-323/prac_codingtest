# 문제에 나온 알고리즘을 입력값 예시인 7을 기준으로
# 첫번째 반복문은 1 - 5까지
# 두번째 반복문은 2 - 6까지
# 세번째 반복문은 3 - 7까지 실행된다.
# 즉, 1 부터 n까지의 숫자 중 3가지를 뽑아 중복없이, 크기 순으로 작성하는 경우의 수가 시간 복잡도를 계산하는 방법이다. -> nC3

import sys as s
a = int(s.stdin.readline().strip())

print(((a * (a - 1) * (a - 2)) // 6))
print(3)

