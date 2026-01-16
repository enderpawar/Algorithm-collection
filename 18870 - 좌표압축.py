import sys

# 1. N 입력 (최대 1,000,000)
n = int(sys.stdin.readline().strip())

# 2. X 좌표들 입력 (리스트 형태)
x_list = list(map(int, sys.stdin.readline().split()))

# 좌표 압축 방법 1. 중복 제거 set 2. 정렬 sort 3. 순위 매기기 dictionary 

# 1. 중복 제거
set(x_list) 
# 2. 정렬
sorted_list =sorted(list(set(x_list)))
# 3. 순위 매기기
dic = {val : i for i, val in enumerate(sorted_list)}

for x in x_list:
    print(dic[x], end=' ')

