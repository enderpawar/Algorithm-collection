import sys
from collections import deque

# 1. 테스트 케이스 개수 입력 (정수 변환 필수)
input_data = sys.stdin.readline().strip()

t = int(input_data)

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    # 변수명 map 대신 field 사용 (내장 함수 map과 충돌 방지)
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    # 2. 배추 위치 기록
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1  # y가 행(row), x가 열(col)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0

    # 3. 맵 전체를 순회하며 배추가 있는 구역 찾기 BFS
    for i in range(n):
        for j in range(m):

            if field[i][j] == 1 and not visited[i][j]:
                count += 1 
                queue = deque([(i ,j)])
                visited[i][j] = 1

                while queue : 
                    y,x = queue.popleft()

                    for d in range(4):
                        ny,nx = y+ dy[d], x+dx[d]

                        if 0 <= ny < n and 0 <= nx <m :
                            if field[ny][nx] ==1 and not visited[ny][nx]:
                                queue.append((nx,ny))
                                visited[ny][nx] = 1
    
    print(count)