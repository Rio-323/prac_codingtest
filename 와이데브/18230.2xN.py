# 입력 받기
n, a, b = map(int, input().split())
one_tiles = sorted(list(map(int, input().split())), reverse=True) if a > 0 else []
two_tiles = sorted(list(map(int, input().split())), reverse=True) if b > 0 else []

# 최대 만족도 저장 변수
result = 0

# n이 홀수인 경우, 1x1 타일 하나를 사용하여 n을 짝수로 만듭니다.
if n % 2 == 1 and one_tiles:
    result += one_tiles.pop(0)
    n -= 1

# 남은 칸을 채우며 최대 만족도 계산
while n >= 2:
    # 1x1 타일 두 개를 사용하는 경우와 1x2 타일 한 개를 사용하는 경우 중 더 큰 만족도를 선택
    option_one = (one_tiles[0] + one_tiles[1] if len(one_tiles) >= 2 else 0)
    option_two = two_tiles[0] if two_tiles else 0
    
    # 더 높은 만족도를 추가하고 해당 타일 제거
    if option_one > option_two:
        result += option_one
        one_tiles.pop(0)
        one_tiles.pop(0)
    else:
        result += option_two
        two_tiles.pop(0)
        
    n -= 2

print(result)