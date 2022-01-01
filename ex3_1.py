money=[500,100,50,10]

N=int(input("입력"))
num=0

for i in money:
    num+=N//i
    N=N%i

print(num)