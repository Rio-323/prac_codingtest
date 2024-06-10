from collections import deque
import sys

input = sys.stdin.read
data = input().strip().split()

n = int(data[0]) # 정점의 수
m = int(data[1]) # 간선의 수
r = int(data[2]) # 시작 정점

edges = []
index = 3
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    edges.append((u, v))
    index += 2

def bfs(n, m, r, edges):
    graph = [[] for _ in range(n + 1)]

    # 간선 정보 입력
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort() # 방문 순서를 위해 정렬

    # 방문 여부와 방문 순서 저장
    visited = [-1] * (n + 1) # -1은 방문하지 않음을 나타냄.
    queue = deque([r]) # 시작 정점 r을 추가
    visited[r] = 1
    order = 1
    result = [0] * (n + 1)

    while queue:
        node = queue.popleft()
        result[node] = order
        order += 1
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                queue.append(neighbor)
                visited[neighbor] = 1

    return result[1:]  # 1번 정점부터 시작

result = bfs(n, m, r, edges)
for res in result:
    print(res)