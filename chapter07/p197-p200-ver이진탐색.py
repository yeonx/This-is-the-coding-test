def binary_search(array,target,start,end):
    mid=(start+end)//2
    if start>end:
        return None
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

N=int(input())
array=list(map(int,input().split()))
array.sort()
M=int(input())

require=list(map(int,input().split()))

for i in range(M):
    k=binary_search(array,require[i],0,N-1)
    if k==None:
        print('no',end=' ')
    else:
        print('yes',end=' ')
