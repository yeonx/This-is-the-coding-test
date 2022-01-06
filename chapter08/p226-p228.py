n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

d=[10001]*(m+1)
d[0]=0

for i in arr:
    for j in range(i,m+1):
        if d[j-i]!=10001:
            d[j]=min(d[j-i]+1,d[j])

if d[m]==10001:
    print(-1)
else:
    print(d[m])
