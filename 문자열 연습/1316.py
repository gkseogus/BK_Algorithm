n = int(input())

lis = []
count = n
for i in range(n):
    lis = list(input())
    for j in range(len(lis)-1):
        if (lis[j] == lis[j+1]):
            pass
        elif (lis[j] in lis[j+1:]):
            count -= 1
            break

print(count)
