'''
num=input()
result=0

for i in range(1,len(num)):
    if i==1:
        if num[i]=='0' or num[i]=='1' or num[i-1]=='0' or num[i-1]=='1':
            result=int(num[i])+int(num[i-1])
        else:
            result=int(num[i])*int(num[i-1])
    else:
        if num[i]=='0' or num[i]=='1':
            result+=int(num[i])
        else:
            result*=int(num[i])
            
print(result)
'''
#답안에 내 풀이보다 더 간단한 방법이 제시되어 있었다
data=input()

#첫 번째 문자를 숫자로 변경하여 대입
result=int(data[0])

for i in range(1,len(data)):
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우 곱하기보다는 더하기 수행
    num=int(data[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num

print(result)
