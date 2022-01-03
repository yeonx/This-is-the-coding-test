N=int(input())

arr=[]
for i in range(N):
    dt=input().split()
    arr.append((dt[0],int(dt[1])))

arr.sort(key=lambda x:x[1])

for i in arr:
    print(i[0],end=' ')
