import time

start_time=time.time()

N,K = map(int,input().split())

count=0

#while N!=1:
#    if N%K==0:
#        N=N//K
#    else:
#        N=N-1
#    count=count+1
#print(count)
#while문을 N이 더이상 나누어 떨어지지 않을때 까지만 돌게하기
while True:
    #(N==K로 나누어떨어지는 수)가 될때까지 1씩 빼기
    target=(N//K)*K
    count+=(N-target)
    N=target
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N<K:
        break
    #K로 나누기
    count+=1
    N=N//K
#마지막으로 남은 수에 대하여 1씩 빼기
count+=(N-1)
print(count)




end_time=time.time()
print("time :",end_time-start_time)
