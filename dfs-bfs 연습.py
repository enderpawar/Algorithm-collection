import sys

from collections import deque

n,m,v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)] #정점 들간의 연결 관게를 저장할 것임

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1): #간선 탐색시 작은 것부터 들어가게 해주어야함
    graph[i].sort() 

visited = [0]*(n+1)

def dfs(s):
    visited[s] = 1
    print(s,end=' ')
    
    for i in graph[s]:
        if not visited[i]:
            dfs(i)

def bfs(s):
    queue = deque([s])
    visited[s] = 1

    while queue:
        v1 = queue.popleft()
        print(v1,end=' ')
        for i in graph[v1]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                
dfs(v)
print()

visited = [0] * (n+1)
bfs(v)
