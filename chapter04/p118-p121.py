#예시 코드를 한 번 읽고 짠 코드
N,M=map(int,input().split())
A,B,d=map(int,input().split())
arr=[[0]*M for _ in range(N)]
total=[]
for i in range(N):
    r=list(map(int,input().split()))
    total.append(r)

def turn():
    global d
    d-=1
    if d==-1:
        d=3


dx=[-1,0,1,0]
dy=[0,1,0,-1]

turn_count=0

while True:
    arr[A][B]=1
    print("arr :", arr)
    turn()

    nA=A+dx[d]
    nB=B+dy[d]
    
    #if nA>=0 and nA<N and nB>=0 and nB<M: # 예시 코드엔 이 부분을 고려하지 않았다 왜?? -> 조건에 맵의 외곽이 항상 바다로 이루어져 있다고 함
    if total[nA][nB]==0 and arr[nA][nB]==0:
        A=nA
        B=nB
        turn_count=0
    elif total[nA][nB]==1 or arr[nA][nB]==1:
        turn_count+=1
    #else:
    #    continue
    
    if turn_count==4:
        nA=A-dx[d]
        nB=B-dy[d]
        
        #if nA>=0 and nA<N and nB>=0 and nB<M:
        if total[nA][nB]==1:
            break
        else:
            A=nA
            B=nB
            turn_count=0
        #else:
        #    break
        
count=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            count+=1
            
print(count)
