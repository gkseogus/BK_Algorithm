a = int(input())

count = 0
i = 0
k = 1
lis = []

for i in range(a):
    k += i*6
    lis.append(k)
    if (a > lis[i]):
        count += 1
    else:
        count += 1
        break
if (a == 1):
    count = 1

print(count)
