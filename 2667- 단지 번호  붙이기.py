N = int(input()) # 지도 크기, N
# '01101' -> [0, 1, 1, 0, 1] 로 변환됨

visited = [[0] * N for _ in range(N)] # 방문한 좌표
graph = [list(map(int, input())) for _ in range(N)] # 좌표 그래프


dx = [-1,1,0,0]  # 이동할 가로 비트마스크
dy = [0,0,-1,1]  # 이동할 세로 비트마스크
  
group = 0 # 단지수 

home = [] # 단지내 집의수
def dfs(a,b): #dfs 정의
    
        visited[a][b] = 1
        home[group-1]+=1

        for i in range(4):
            na = a+dx[i]
            nb = b+dy[i]
            
            if 0 <= na < N and 0 <= nb < N: # 지도를 벗어나지 않는지 확인해야한다! 이걸 놓쳤네
                if graph[na][nb] == 1 and not visited[na][nb]:
                    dfs(na,nb)
              

for a in range(N): #그래프 탐색하기
     for b in range(N):
        if graph[a][b] == 1 and not visited[a][b]:
             group += 1
             home.append(0)
             dfs(a,b) 

print(group)
home.sort()
for a in home:
     print(a)