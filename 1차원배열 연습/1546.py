n = int(input())
list1 = list(map(int,input().split()))
max = list1[0]
sum = 0

for i in list1[1:]:
    if( i > max):
        max = i
for i in range(n):
    list1[i] = (list1[i]/max)*100
    sum += list1[i]

avg = sum/n
print(avg)


