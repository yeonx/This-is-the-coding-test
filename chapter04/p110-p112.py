N= int(input())

#str_list=list(map(str,input().split()))
#문자 입력 받는 것을 다음과 같이 할 수 있다
str_list=input().split()


x=1
y=1

"""for i in range(6):
    if str_list[i]=='U':
        if y!=1:
            y=y-1
    elif str_list[i]=='D':
        if y!=N:
            y=y+1
    elif str_list[i]=='R':
        if x!=N:
            x=x+1
    elif str_list[i]=='L':
        if x!=1:
            x=x-1
"""
# 이를 다음과 같이 사용
# L,R,U,D에 따른 이동 방향
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']
#이동 계획을 하나씩 확인
for plan in str_list:
    #이동 후 좌표 구하기
    for i in range(4):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
        
        #공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    #이동 수행
    x,y=nx,ny


print(x, y)
