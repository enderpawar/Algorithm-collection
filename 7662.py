# D 1 -> Q에서 최댓값을 삭제하는 연산 -> 즉 D는 Delete임
# D-1 -> Q에서 최솟값을 삭제하는 연산'
# I n 은 정수 n을 Q에 삽입하는 연산을 의미 -> Input
import sys
import heapq


t = int(sys.stdin.readline()) # int 안해주면 에러남 "2\n" 이런식으로 이뤄지기 때문에

for _ in range(t):
    min_heap = [] #최소 힙
    max_heap = [] #최대 힙

    k = int(sys.stdin.readline()) # 이하동문

    visited = [False] * k

    for i in range(k):
        line = sys.stdin.readline().split()

        if line[0] == 'I':
            heapq.heappush(min_heap,(int(line[1]),i))
            heapq.heappush(max_heap,(-int(line[1]),i))
            visited[i] = 1

        elif line[0] == 'D':
            if line[1] == '1': #최대값을 삭제하는 연산
                # [추가] 1. max_heap 꼭대기에 있는 '이미 삭제된 놈'들 청소
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                    # 2. 진짜 삭제
                if max_heap: #max_heap이 비어있지 않으면
                    _ , idx = heapq.heappop(max_heap) 
                    visited[idx] = 0

             #이하 동문
            elif line[1] == '-1': #최솟값을 삭제하는 연산
                while min_heap and not visited[min_heap[0][1]]: #i 번째 수를 방문 안했다면
                    heapq.heappop(min_heap)

                if min_heap:
                    _ , idx = heapq.heappop(min_heap)
                    visited[idx] = 0 #상대 힙에게 삭제됐음을 알림, 한쪽에서만 뻈으니 상대쪽에도 알려주는 용도로 visited 사용

        #중요!!! 청소를 해줘야한다! 힙 꼭대기에 필요없는 정크 데이터가 있으므로
    while max_heap and not visited[max_heap[0][1]]: #들여쓰기 실수하여 반복문 k안에 있었음..
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)        

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")



#출력 : 각 테스트 케이스에 대해 Q에 남아있는 값들 중 최댓값과 최솟값 출력, 비어있으면 EMPTY