from collections import deque

n,k = map(int, input().split())

queue = deque()

queue.append(n)
visited = [-1]* 100001

visited[n]=0

def bfs(a):
    while queue:    
        curr = queue.popleft()      

        if curr == k:
           print(visited[curr])
           break

        for next_pos in (curr-1,curr+1,curr*2):
            if 0<= next_pos <= 100000 and visited[next_pos]==-1: # 범위 제한 꼭 해주자 ㅠㅠ
                    visited[next_pos]=visited[curr]+1
                    queue.append(next_pos)
    
bfs(n)