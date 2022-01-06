n=int(input())

d=[0]*(n+1)

d[1]=1
d[2]=3

#틀렸던 나의 코드,,
'''
for i in range(3,n+1):
    if i%2==1:
        d[i]=d[i-1]+2
    else:
        d[i]=d[i-2]*d[2]*2
'''
for i in range(3,n+1):
        d[i]=d[i-1]+2*d[i-2]

print(d[n]%796796)
