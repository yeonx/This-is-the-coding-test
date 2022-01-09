'''
N=int(input())

arr=list(map(int,input().split()))

arr.sort()

result=0

print(arr)
count=0
i=0
while True:
    if i==N:
        break
    if count==0:
        max=arr[i]
    else:
        if max<arr[i]:
            max=arr[i]
    count+=1
    print(i,max,count,result)
    if max==count:
        count=0
        result+=1

    i+=1

print(result)
'''

#공포도가 같은 경우만 판단해서 답에 넣어보면 오답이 나왔을 것이다.
n=int(input())
data=list(map(int,input().split()))
data.sort()

result=0

count=0

for i in data:
    count+=1
    if count>=i:
        result+=1
        count=0

print(result)
