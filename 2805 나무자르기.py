import sys

n,m = map(int, sys.stdin.readline().split()) # n: 통나무 수 m: 집으로 가져가려하는 통나무 길이
log = list(map(int, sys.stdin.readline().split()))

#이분탐색 하기
low=0
high=max(log)
result=0

while low <= high:
    mid = (low+high) // 2
    total = 0

    for x in log:
        if x > mid:
            total+=x-mid

    if total>=m :
        result = mid
        low = mid+1 
    else:
        high = mid-1 

print(result)