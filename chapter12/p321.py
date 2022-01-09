N=int(input())

le=0
ri=0

n=N
count=0
while n!=0:
    count+=1
    n=n//10

count=count//2

for i in range(count):
    ri+=N%10
    N=N//10
for i in range(count):
    le+=N%10
    N=N//10
if le==ri:
    print("LUCKY")
else:
    print("READY")


