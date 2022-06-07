x = int(input())

lst = []
count = 0

for i in range(0, x):
    lst.append(input())
print(lst)

for i in lst:
    if(i > 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
            else:
                count += 1
print(count)
