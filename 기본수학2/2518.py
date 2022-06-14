m = int(input())
n = int(input())
lst = []

for i in range(m, n+1):
    count = 0
    if i > 1:
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
            if count == 2:
                lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
