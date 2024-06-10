import sys
input = sys.stdin.read
sys.setrecursionlimit(10 ** 6)

def dfs(graph, start):
    visited = [False] * len(graph) # 방문여부를 표시할 배열
    order = [0] * len(graph) # 방문 순서릴 기록할 배열
    stack = [start] # 시작 노드 추가
    cnt = 1

    while stack: # 스택이 빌때까지 반복
        node = stack.pop() # 탐색할 노드를 가져옴
        if not visited[node]: # 노드 방문하지 않았다면
            visited[node] = True # 노드를 방문으로 표시
            order[node] = cnt # 방문 순서 기록
            cnt += 1
            for next_node in sorted(graph[node], reverse=True): # 스택에서 작은 노드부터 방문하기 위해 역순으로 정렬
                if not visited[next_node]: # 방문한 노드인지 확인
                    stack.append(next_node)

    return order

data = input().split()
N, M, R = int(data[0]), int(data[1]), int(data[2]) # 그래프의 크기와 시작점 설정

graph = [[] for _ in range(N + 1)]
index = 3 # u, v 를 받아오기 위해

for _ in range(M):
    u, v = int(data[index]), int(data[index + 1])
    graph[u].append(v) # 그래프에 추가
    graph[v].append(u)
    index += 2 # 다음으로 이동

order = dfs(graph, R)

for i in range(1, N + 1):
    print(order[i])