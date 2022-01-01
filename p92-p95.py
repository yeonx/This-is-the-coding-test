#N=int(input())
#M=int(input())
#K=int(input())
#이 부분을 공백으로 받기 위해서
N,M,K=map(int,input().split())


#num_list=[]
#for i in range(N):
#    a=int(input())
#    num_list.append(a)
#이 부분을 공백으로 받기 위해서
num_list=list(map(int,input().split()))

num_list.sort()
a=num_list[N-1]
b=num_list[N-2]

K=K+1
num=M//K
last_num=M%K

max=(a*(K-1)+b)*num +a*last_num

print(max)
