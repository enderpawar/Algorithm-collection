import sys 

# N,M입력
n,m = map(int, sys.stdin.readline().split())

board = [list(map(int,input().split())) for _ in range(n)] # 전체 좌표별 값

visited = [[False] * m for _ in range(n)] #방문 흔적

max_val = 0 #최댓값

res = 0 # 결과

#방향 벡터
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,depth,current_sum):

    global res 
    if depth == 4: # 종료 조건 : 깊이 4
        res = max(res,current_sum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # ㅗ 모양 찾기 트릭 -> 제자리에서 3번째칸 찾기
            if depth == 2:
                visited[nx][ny] = True
                dfs(x, y, depth + 1, current_sum + board[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = 1
            
            dfs(nx, ny, depth+1, current_sum + board[nx][ny])     

            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0 #방문 표시다시 풀어줘야함. 왜? 다른 점들도 탐색해야할거아냐

print(res)