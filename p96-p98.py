import time
start_time=time.time()

N,M=map(int,input().split())

k=0

for i in range(N):
    num_list=list(map(int,input().split()))
    a=min(num_list) #현재 줄에서 가장 작은 수 찾기
    #if a>k:
    #    k=a;
    # 가장 작은 수로 뽑아 낸 것 중 큰 수 찾기
    k=max(a,k)
        
print(k)

end_time=time.time()
print("time :",end_time-start_time)
