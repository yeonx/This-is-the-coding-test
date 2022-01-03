arr=[5,7,9,0,1,6,2,4,8]

def quick_sort(arr):
    
    if len(arr)<=1:
        return arr
    
    pivot=arr[0] #피벗은 첫 원소
    tail=arr[1:] #피벗을 제외한 리스트
    
    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]
    
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))
