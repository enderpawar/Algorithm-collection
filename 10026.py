import sys
from collections import deque

n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

def bfs():
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count += 1
                queue = deque([(i, j)])
                visited[i][j] = True
                color = grid[i][j]

                while queue:
                    x, y = queue.popleft()

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < n:
                            # 괄호 추가: (nx, ny)
                            if not visited[nx][ny] and grid[nx][ny] == color:
                                visited[nx][ny] = True 
                                queue.append((nx, ny)) 
    return count

# 1. 일반인 결과 출력
print(bfs(), end=' ')

# 2. 적록색약용 데이터 보정 (G를 R로 교체)
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R' # 대입 연산자(=)로 수정

# 3. 적록색약 결과 출력
print(bfs())