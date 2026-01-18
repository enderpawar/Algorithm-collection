import sys
from collections import deque

# 1. 입력 받기
m, n, h = map(int, sys.stdin.readline().split())

# 2. 3차원 그래프 입력 및 시작점(익은 토마토) 찾기
graph = []
queue = deque()

for i in range(h):
    layer = []
    for j in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if row[k] == 1:
                # 익은 토마토 위치를 큐에 담기 (높이, 세로, 가로)
                queue.append((i, j, k))
        layer.append(row)
    graph.append(layer)

# 3. 6방향 탐색 설정 (위, 아래, 앞, 뒤, 좌, 우)
dh = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dm = [0, 0, 0, 0, 1, -1]

# 4. BFS 수행
while queue:
    curr_h, curr_n, curr_m = queue.popleft()
    
    for i in range(6):
        nh = curr_h + dh[i]
        nn = curr_n + dn[i]
        nm = curr_m + dm[i]
        
        # 범위 내에 있고, 익지 않은 토마토(0)라면
        if 0 <= nh < h and 0 <= nn < n and 0 <= nm < m:
            if graph[nh][nn][nm] == 0:
                # 익음 처리하고 이전 값 + 1 (날짜 카운트)
                graph[nh][nn][nm] = graph[curr_h][curr_n][curr_m] + 1
                queue.append((nh, nn, nm))

# 5. 결과 확인
max_days = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 토마토가 다 익지 못한 경우
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            # 가장 오래 걸린 날짜 찾기
            max_days = max(max_days, graph[i][j][k])

# 처음 시작이 1이었으므로 1을 빼줘야 실제 경과 일수가 나옴
if max_days == 1:
    print(0) # 처음부터 다 익어있었던 경우
else:
    print(max_days - 1)