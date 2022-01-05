n,m=map(int,input().split())
array=list(map(int,input().split()))
array.sort()
start=0
end=array[n-1]
while True:
    mid=(start+end)//2
    total=0
    for data in array:
        if data>mid:
            total=total+data-mid
    if total==m:
        result=mid
        break
    elif total>m:
        start=mid+1
    else:
        end=mid-1
print(result)
