from collections import deque

N,M=map(int,input().split())

graph=[]
for i in range(N):
    graph.append(list(map(int,input())))


x,y=0,0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
queue=deque()

def bfs():
    queue.append((0,0))
    #큐가 빌 때까지 반복
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            #미로의 찾기 공간을 벗어난 경우 무시
            if ny<0 or nx<0 or ny==M or nx==N:
                continue
            #벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[N-1][M-1]

print(bfs())
