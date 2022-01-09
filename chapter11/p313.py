data=input()

c=data[0]

reverse=0

for i in range(len(data)):
    if c!=data[i]:
        c=data[i]
        reverse+=1

print((reverse+1)//2)
