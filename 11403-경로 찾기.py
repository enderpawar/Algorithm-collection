import sys

# 1. 정점의 개수 N 입력
N = int(sys.stdin.readline().strip())

# 2. 인접 행렬 입력 (2차원 리스트)
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 3. 플로이드-워셜 알고리즘 적용
# k: 거쳐가는 노드 (징검다리)
for k in range(N):
    # i: 출발 노드
    for i in range(N):
        # j: 도착 노드
        for j in range(N):
            # i에서 k로 갈 수 있고, k에서 j로 갈 수 있다면
            # i에서 j로 가는 경로가 존재한다고 판단(1)
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

# 4. 결과 출력 (행별로 출력)
for row in graph:
    print(*row)