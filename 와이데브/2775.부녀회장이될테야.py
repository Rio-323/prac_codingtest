num = int(input())

for _ in range(num):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n + 1)] # 0층 사람 수 초기화 (1호에 1명, 2호에 2명...)

    for _ in range(k): # k층까지 계산
        for j in range(1, n): # 각 호수에 대해 계산
            people[j] += people[j - 1]
    
    print(people[-1])