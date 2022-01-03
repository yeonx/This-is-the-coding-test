'''
N=int(input())

arr=[]

for i in range(N):
    arr.append(int(input()))

arr.sort()
arr.reverse()

for i in arr:
    print(i, end=' ')
'''
N=int(input())

arr=[]
for i in range(N):
    arr.append(int(input()))

arr=sorted(arr,reverse=True)

for i in arr:
    print(i, end=' ')
