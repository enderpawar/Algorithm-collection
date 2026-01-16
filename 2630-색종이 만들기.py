import sys

n = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0 
blue = 0

def div(x, y, n): # x, y: 시작 좌표 / n: 현재 크기
    global white, blue
    
    # 1. 기준 색상 정하기 (현재 사각형의 맨 왼쪽 위 칸)
    base_color = paper[x][y]
    
    # 2. 현재 영역(x~x+n, y~y+n)을 탐색
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 기준 색상과 다른 게 하나라도 나오면
            if paper[i][j] != base_color:
                # 3. 4등분해서 다시 던지기
                half = n // 2
                div(x, y, half)               # 1사분면 (왼위)
                div(x, y + half, half)        # 2사분면 (오위)
                div(x + half, y, half)        # 3사분면 (왼아래)
                div(x + half, y + half, half) # 4사분면 (오아래)
                return # 중요! 쪼개서 들어갔다 왔으면 현재 함수는 종료해야 함
    
    # 4. 반복문을 무사히 마쳤다면 (모든 칸이 같은 색)
    if base_color == 0:
        white += 1
    else:
        blue += 1

# 처음에 전체 크기로 시작!
div(0, 0, n)

print(white)
print(blue)