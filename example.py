
# 인접 리스트로 그래프 구현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 깊이 우선 탐색 (DFS) - 재귀적 구현
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)

print("DFS 탐색 순서:")
dfs(graph, 'A')


from collections import deque

# 인접 리스트로 그래프 구현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 너비 우선 탐색 (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

print("BFS 탐색 순서:")
bfs(graph, 'A')