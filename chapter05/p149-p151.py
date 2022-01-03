'''
N,M=map(int,input().split())

graph=[]

for i in range(N):
    graph.append(list(map(int,input()))) #이 표현 기억하기..
    

visited=[[False]*M for _ in range(N)]

def dfs(visited,i,j):
    if i<0 or j<0 or i>=N or j>=M:
        return 0
    if graph[i][j]==1:
        return 0
    visited[i][j]=True
    graph[i][j]=1
    dfs(visited,i-1,j)
    dfs(visited,i+1,j)
    dfs(visited,i,j-1)
    dfs(visited,i,j+1)
    return 1
    
result=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            dfs(visited,i,j)
            result+=1
            
print(result)
'''
N,M=map(int,input().split())

graph=[]

for i in range(N):
    graph.append(list(map(int,input()))) #이 표현 기억하기..

def dfs(i,j):
    if i<0 or j<0 or i>=N or j>=M:
        return 0
    if graph[i][j]==1:
        return 0
    graph[i][j]=1
    dfs(i-1,j)
    dfs(i+1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    return 1
    
result=0
for i in range(N):
    for j in range(M):
        if dfs(i,j)==1:
            result+=1
            
print(result)
