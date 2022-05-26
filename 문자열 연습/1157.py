a = input().upper()
a_b = list(set(a))
lst = []

for i in a_b:
    lst.append(a.count(i))

if (lst.count(max(lst)) > 1):
    print('?')
else:
    index = lst.index(max(lst))
    print(a_b[index])
