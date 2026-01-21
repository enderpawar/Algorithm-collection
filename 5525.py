import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

ans = 0    # 정답 개수
cnt = 0    # 연속된 'IOI'의 개수
i = 1      # 인덱스 포인터

while i < m - 1:
    # 3글자씩 끊어서 'IOI'인지 확인 (인덱스 직접 접근)
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        cnt += 1
        
        # 원하는 만큼 IOI가 반복되었다면
        if cnt == n:
            ans += 1
            cnt -= 1 # 다음 중첩 확인을 위해 하나만 뺌 (중요!)
        
        i += 2 # IOI 확인했으니 2칸 점프
    else:
        cnt = 0 # 패턴이 깨지면 리셋
        i += 1  # 다음 칸 탐색

print(ans)