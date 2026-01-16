s=input().split('-') #문자열 형태로 저장된다

res = []
for a in s:
    if "+" in a:
        arr = a.split("+")  
        temp = sum(map(int,arr))
        res.append(temp)
    else:
        res.append(int(a))   

result = int(res[0])*2

for a in res:
     result-=int(a)
print(result)  