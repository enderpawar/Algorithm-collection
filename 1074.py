import sys

# 1. 입력 받기
n, r, c = map(int, sys.stdin.readline().split())

ans = 0

# 2. n이 0이 될 때까지 사각형을 쪼개며 좌표 추적
while n > 0:
    # 한 변의 길이의 절반 (n=3이면 2^2 = 4)
    half = 2 ** (n - 1)
    # 한 조각(사분면)의 넓이
    area = half * half
    
    # [1사분면] 왼쪽 위
    if r < half and c < half:
        # 아무것도 더하지 않고 다음 단계로 진입
        pass
        
    # [2사분면] 오른쪽 위
    elif r < half and c >= half:
        ans += area # 1사분면 넓이만큼 건너뛰기
        c -= half   # 좌표를 1사분면 위치로 보정
        
    # [3사분면] 왼쪽 아래
    elif r >= half and c < half:
        ans += area * 2 # 1, 2사분면 넓이만큼 건너뛰기
        r -= half       # 좌표를 1사분면 위치로 보정
        
    # [4사분면] 오른쪽 아래
    else:
        ans += area * 3 # 1, 2, 3사분면 넓이만큼 건너뛰기
        r -= half       # 좌표 보정
        c -= half       # 좌표 보정
        
    # 사각형 크기를 줄여서 다시 반복
    n -= 1

print(ans)