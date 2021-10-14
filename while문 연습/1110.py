n = int(input())
sum = n
cnt = 0
while True:
    a = sum//10
    b = sum%10
    c = (a+b)%10
    sum = (b*10) + c 
    cnt += 1
    if (sum == n):
        break
print(cnt)
    #자릿수 확인 코드
    # for i in range(len(n)):
    #     print(n[i])  
    #     sum += int(n[i])
    #     cnt += 1
    #     print(sum)
    
