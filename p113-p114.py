"""
N=int(input())

total=60*60*(N+1)

three_list_ms=[3,13,23,43,53,
            30,31,32,33,34,35,36,37,38,39]
three_list_h=[3,13,23]

for i in range(N+1):
    if i not in three_list_h:
        print(i)
        total-=(60-len(three_list_ms))*(60-len(three_list_ms))
        
print(total)
"""

# 답안- 근데 내가 푼게 더 마음에 든다
h=int(input())
count=0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)
