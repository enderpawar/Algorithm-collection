import sys
input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
fruits = list(map(int, input().split()))

# 2. 돋보기(구간) 설정
left = 0
max_len = 0
count = {} # 과일 종류별 개수를 담을 주머니

for right in range(n):
    # 오른쪽 과일을 주머니에 넣기 (종류 카운트)
    f_right = fruits[right]
    count[f_right] = count.get(f_right, 0) + 1 #get(key, default) -> f_right가 count에 있으면 저장된 개수를, 없으면 0 을 가져오기 
    
    # 종류 수가 2개를 넘으면 왼쪽을 뺀다!
    while len(count) > 2:
        f_left = fruits[left]
        count[f_left] -= 1
        
        # 개수가 0이 되면 주머니에서 완전히 비워야 '종류 수'가 줄어듦
        if count[f_left] == 0:
            del count[f_left]
        
        left += 1 # 왼쪽 포인터 이동
        
    # 현재 두 종류 이하인 구간의 길이를 재서 최댓값 비교
    max_len = max(max_len, right - left + 1)

print(max_len)