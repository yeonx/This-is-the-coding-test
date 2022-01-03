'''
N,K=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

hap=0
for i in range(N):
    if i<K:
        hap+=B[i]
    else:
        hap+=A[i]
        
print(hap)
'''

N,K=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i]<B[i]:
        A[i],B[i]=B[i],A[i]
    else:
        break
        
print(sum(A))
