list1 = []

for i in range(10):
    a = int(input())
    a = a%42
    list1.append(a)

print(len(set(list1)))