'''
arr=list(input())
print(arr)
print(len(arr))
result=0

array=[]

for i in range(len(arr)):
    if arr[i]>='0' and arr[i]<='9':
        result+=int(arr[i])
    else:
        array.append(arr[i])
array.sort()
strA="".join(array)
print(strA,end='')
print(result)
'''
#내 코드에선 숫자가 없을 경우를 생각하지 못했다

data=input()
result=[]
value=0

#문자를 하나씩 확인하며
for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    #숫자는 따로 더하기
    else:
        value+=int(x)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value!=0:
    result.append(str(value))

#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
