import sys
input = sys.stdin.read

# 입력 받기
board = [list(map(int, line.split())) for line in input().strip().splitlines()]

# 방향 배열 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 중복 없이 숫자를 저장할 집합
unique_numbers = set()

# DFS 함수 정의
def dfs(x, y, number):
    # 숫자가 6자리가 되면 set에 추가
    if len(number) == 6:
        unique_numbers.add(number)
        return

    # 상하좌우로 이동하며 숫자 생성
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 숫자판 내에서만 이동 가능
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number + str(board[nx][ny]))

# 각 위치에서 DFS 탐색 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, str(board[i][j]))

# 결과 출력
print(len(unique_numbers))