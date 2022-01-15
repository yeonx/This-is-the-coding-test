'''
N=int(input())

arr=list(map(int,input().split()))

def heap(start,end):
    if start>end:
        print(-1)
        return
    left=arr[start]
    right=arr[end]
    mid=arr[(start+end)//2]
    if mid==(start+end)//2:
        print(mid)
        return
    elif (start+end)//2<mid:
        heap(start,(start+end)//2-1)
    else:
        heap((start+end)//2+1,end)

heap(0,N-1)
'''
#내 코드도 잘 동작하지만 확인할 수 없으니 답안 확인

from operator import index


def binary_search(array,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    #고정점을 찾은 경우 인덱스 반환
    if array[mid]==mid:
        return mid
    #중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid]>mid:
        return binary_search(array,mid+1,end)
    
n=int(input())
array=list(map(int,input().split()))

#이진 탐색 수행
index=binary_search(array,0,n-1)

#고정점이 없는 경우 -1출력
if index==None:
    print(-1)
else:
    print(index)
