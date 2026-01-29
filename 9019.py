import sys
from collections import deque
# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.


#1. DSLR 함수 각각 정의
def D(n):
    res = n*2
    if res > 9999:
        return res % 10000 #2n mod 10000
    else:
        return res
def S(n):
    if n == 0:
        return 9999
    else:
        return n-1
def L(n):
    next_n = (n % 1000) * 10 + (n // 1000) #arr 자리수별로 분리하기 보단... 맨 앞만 떼서 뒤로 보낸다는 느낌으로.
    return next_n

def R(n): 
    next_n = (n % 10) * 1000 + (n // 10)
    return next_n

#2. BFS 정의

def BFS(a,b):
        # 큐에 시작값, 경로를 담기
        queue = deque([(a,"")])

        # 방문 체크를 위한 배열 
        visited = [False] *10000
        visited[a] = 1
        
        # dx = [1,-1,0,0] 이건 필요없다. 방향 찾기가 아니니까.
        # dy = [0,0,1,-1]
        
        while queue: #큐가 끝날때까지
            curr, path = queue.popleft() #현재 값, 여태까지 한 연산

            if curr == b:
                return path    
            
            next_states = [
                (D(curr),"D"),
                (S(curr),"S"),
                (L(curr),"L"),
                (R(curr),"R") # next_n(다음 값), cmd(커맨드)
            ]
            
            for next_n,cmd in next_states:
                if not visited[next_n]:
                    visited[next_n] = 1
                    queue.append((next_n, path + cmd))

#3. 메인함수
T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(BFS(a,b))
