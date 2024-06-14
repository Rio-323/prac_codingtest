import sys as s

n = 1000 - int(s.stdin.readline().strip())
money_list = [500, 100, 50, 10, 5, 1]  # 사용 가능한 동전 단위
count = 0  # 총 동전 개수

for i in money_list:
    if n >= i:  # 잔돈이 현재 동전 단위보다 크거나 같을 때만 처리
        count += n // i  # 현재 동전 단위로 거슬러 줄 동전 개수 추가
        n %= i  # 남은 잔돈 업데이트

print(count)  # 총 동전 개수 출력