"""
point=input()
first=point[0]
second=point[1]
if first>='c' and first<='f':
    if second>='3' and second<='6':
        count=8
    else:
        count=4
else:
    if second>='3' and second<='6':
        count=4
    else:
        count=2
        
print(count)
"""
#한가지 경우를 고려 안해서 답이 틀림!!


#현재 나이트의 위치 입력받기
input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1 #int를 해준것과 안해준 것의 차이는 없지만 알아두기

#나이트가 이동할 수 있는 8가지 방향 정의
steps=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result=0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row=row+step[0]
    next_column=column+step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1
print(result)
