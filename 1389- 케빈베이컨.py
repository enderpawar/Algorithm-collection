import sys
from collections import deque

input = sys.stdin.readline

# 1. N(사람 수), M(관계 수) 입력
n, m = map(int, input().split())

# 2. 인접 리스트 만들기 (1번~N번까지 사용하기 위해 n+1)
adj = [[] for _ in range(n+1)]

# 3. M개의 친구 관계 입력받아 저장하기
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u) # 친구는 양방향!

# 4. 각 사람의 점수를 담을 리스트 (인덱스 맞추기 위해 n+1)
bacon_counts = [0] * (n+1)

def bfs(a):
    # 1. 거리 기록지 (visited 역할 겸 거리 저장)
    dist = [-1] * (n+1)
    dist[a] = 0 

    queue = deque([a])              

    while queue:
        curr = queue.popleft()

        for neighbor in adj[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)

    return sum(dist) + 1 # 각 정점의 베이컨 값들 정리 

for i in range(1,n+1):
    bacon_counts[i] = bfs(i)

bacon_counts[0] = 999999999 #0에 가장 큰 값 넣기

min_score = min(bacon_counts)
print(bacon_counts.index(min_score))

