import sys 
from collections import deque

line = sys.stdin.readline().split()
if not line: exit() # 입력 예외 처리
n, m = int(line[0]), int(line[1])

graph = []

start_x, start_y = -1, -1

for i in range(n):
    # 한 줄씩 읽어서 리스트로 변환
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

    if 2 in row:
         start_x, start_y = i, row.index(2)

result_graph =[[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result_graph[i][j] = 0
    
#BFS
queue = deque([(start_x,start_y)])
result_graph[start_x][start_y] = 0


#방향 벡터 생성
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue:
    x,y = queue.popleft()
    
    for i in range(4):
        moved_x = x+dx[i]
        moved_y = y+dy[i]

        if 0 <= moved_x < n and 0 <= moved_y < m:
            if result_graph[moved_x][moved_y] == -1 and graph[moved_x][moved_y] == 1: 
                queue.append((moved_x,moved_y)) 
                result_graph[moved_x][moved_y]=result_graph[x][y]+1
    
for row in result_graph:
    print(*row)
              
            

       
        
    