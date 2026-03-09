import sys 

# 파이썬 재귀 깊이 제한 해제
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline()) # n 집의 크기 !놓친 포인트 1 : int로 안감쌌다..

board = [[0] * (n + 1)] # -> 맵 정보 0은 빈칸 1은 벽

for _ in range(n):
    # 각 줄의 맨 앞에 0을 추가해서 1번 열부터 시작하게 만듦
    row = [0] + list(map(int, sys.stdin.readline().split()))
    board.append(row)
    
dp = [[[-1] * 3 for _ in range(n + 1)] for _ in range(n + 1)] # 1번 인덱스부터 쓸거임
# 3차원 배열로 현재 좌표 y,x (행 열) 와 방향 0 가로 / 1 대각선 / 2 세로 으로 해야함

# 1. 모든 경우의 수 구해질때까지 반복
def move(y,x,d):
    if y == n and x == n:
        return 1
    
    # 이미 계산했으면 결과 반환 (메모이제이션)
    if dp[y][x][d] != -1:
        return dp[y][x][d]

    res = 0

    # 1. 방향이 가로 0 일때
    if d == 0:
        # 1 - 가로로 이동
        if x + 1 <= n:
            if board[y][x+1] != 1:
                res += move(y,x+1,0) 
        # 2 - 대각선으로 이동
        if x + 1 <= n and y + 1 <= n:
            if board[y+1][x+1] != 1 and board[y][x+1] !=1 and board[y+1][x] !=1:
                res += move(y+1,x+1,1)
    
    # 2. 방향이 대각선 1 일때
    if d == 1:
        # 1 - 가로로 이동
        if x + 1 <= n:
            if board[y][x+1] != 1:
                res += move(y,x+1,0)
        # 2 - 세로 아래로 이동 
        if y + 1 <= n:
            if board[y+1][x] != 1:
                res += move(y+1,x,2)
        # 3 - 대각선으로 이동
        if x + 1 <= n and y + 1 <= n:
            if board[y+1][x+1] != 1 and board[y][x+1] !=1 and board[y+1][x] !=1:
                res += move(y+1,x+1,1)

    if d == 2:
        # 2 - 세로 아래로 이동 
        if y + 1 <= n:
            if board[y+1][x] != 1:
                res += move(y+1,x,2)
        # 3 - 대각선으로 이동
        if x + 1 <= n and y + 1 <= n:
            if board[y+1][x+1] != 1 and board[y][x+1] !=1 and board[y+1][x] !=1:
                res += move(y+1,x+1,1)
    
    # 결과 저장 후 리턴
    dp[y][x][d] = res
    return res

# 시작 지점 (1, 2)에서 가로(0) 방향으로 시작
print(move(1,2,0))