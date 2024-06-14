import heapq  # 힙큐 모듈을 임포트하여 우선순위 큐로 사용
import sys
input = sys.stdin.read  # 표준 입력을 읽기 위한 설정
INF = int(1e9)  # 무한대를 나타내는 큰 값

def dijkstra(start, graph, n):
    distances = [INF] * (n + 1)  # 모든 노드까지의 거리를 무한대로 초기화
    distances[start] = 0  # 시작 노드까지의 거리는 0으로 설정
    pq = [(0, start)]  # 우선순위 큐에 시작 노드를 추가

    while pq:  # 큐가 비어있지 않은 동안 반복
        current_distance, current_node = heapq.heappop(pq)  # 가장 짧은 거리의 노드를 꺼냄
        if current_distance > distances[current_node]:  # 이미 처리된 노드는 무시
            continue
        for adjacent, weight in graph[current_node]:  # 현재 노드의 인접 노드를 확인
            distance = current_distance + weight  # 새로운 거리 계산
            if distance < distances[adjacent]:  # 더 짧은 경로를 발견하면 업데이트
                distances[adjacent] = distance
                heapq.heappush(pq, (distance, adjacent))  # 큐에 새로운 경로 추가
    return distances  # 시작 노드로부터 모든 노드까지의 최단 거리 반환

data = input().split()  # 입력 데이터를 공백으로 분리
N = int(data[0])  # 노드의 수
E = int(data[1])  # 간선의 수

graph = [[] for _ in range(N + 1)]  # 노드 수만큼의 빈 리스트 생성

index = 2  # 데이터 인덱스 초기화
for _ in range(E):
    a = int(data[index])  # 간선의 시작 노드
    b = int(data[index + 1])  # 간선의 끝 노드
    c = int(data[index + 2])  # 간선의 가중치
    graph[a].append((b, c))  # 양방향 간선 추가
    graph[b].append((a, c))
    index += 3  # 인덱스 증가

v1 = int(data[index])  # 반드시 거쳐야 하는 첫 번째 노드
v2 = int(data[index + 1])  # 반드시 거쳐야 하는 두 번째 노드

dist_start = dijkstra(1, graph, N)  # 시작 노드로부터 최단 거리 계산
dist_v1 = dijkstra(v1, graph, N)  # v1 노드로부터 최단 거리 계산
dist_v2 = dijkstra(v2, graph, N)  # v2 노드로부터 최단 거리 계산

path1 = dist_start[v1] + dist_v1[v2] + dist_v2[N]  # 경로 1: 1 -> v1 -> v2 -> N
path2 = dist_start[v2] + dist_v2[v1] + dist_v1[N]  # 경로 2: 1 -> v2 -> v1 -> N

result = min(path1, path2)  # 두 경로 중 최소 값 선택

if result >= INF:  # 경로가 존재하지 않으면
    print(-1)
else:
    print(result)  # 최단 경로 출력