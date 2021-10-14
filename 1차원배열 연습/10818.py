n = int(input())
list1 = list(map(int, input().split()))
max = list1[0]
min = list1[0]

for i in list1[1:]:
    if( i > max):
        max = i
    elif( i < min):
        min = i
print(min,max)