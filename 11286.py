import heapq
import sys

# 1. 힙으로 사용할 리스트 생성
abs_heap = []

n = int(sys.stdin.readline())

for _ in range(n):

    x = int(sys.stdin.readline())

    if x != 0:
        # 2. heapq.heappush(리스트, (정렬기준1, 정렬기준2, ...))
        # 절댓값을 1순위, 실제 값을 2순위로 정렬하도록 튜플로 넣기.
        heapq.heappush(abs_heap, (abs(x),x))

    else:
        # 3. 힙이 비어있는지 확인
        if not abs_heap:
            print(0)
        else:
            # 4. heapq.heappop(리스트)
            # 가장 우선순위가 높은(값이 작은) 튜플이 나오고, 
            # 우리는 실제 값인 [1]번 인덱스를 출력.
            print(heapq.heappop(abs_heap)[1])
        