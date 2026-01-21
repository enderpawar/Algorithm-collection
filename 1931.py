import sys

# 1. 입력 받기
n = int(sys.stdin.readline())
meetings = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

# 2. 정렬 
# 1순위: 끝나는 시간(x[1]) 기준 오름차순
# 2순위: 끝나는 시간이 같다면 시작 시간(x[0]) 기준 오름차순
meetings.sort(key = lambda x : (x[1],x[0]))

# 3. 회의 선택하기
count = 0        # 선택된 회의의 개수
last_end_time = 0 # 마지막 회의가 끝난 시간

for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end
# 4. 결과 출력
print(count)