A, B = map(int, input().split())
sequence = []
for i in range(1, B + 1):
    for j in range(i):
        sequence.append(i)


result = sum(sequence[A-1:B])
print(result)


# 더 빠른 방법
sequence = []

# 최대 범위는 1000까지 필요한 숫자를 채우기 위해 충분한 범위로 설정합니다.
max_value = 50  # 실제로 필요한 만큼의 수열을 만들기 위해 임의로 설정.

for i in range(1, max_value + 1):
    sequence.extend([i] * i)  # i를 i번 반복해서 sequence 리스트에 추가

A, B = map(int, input().split())

# 수열의 A번째부터 B번째까지의 합을 계산합니다.
result = sum(sequence[A-1:B])

print(result)  # 결과 출력