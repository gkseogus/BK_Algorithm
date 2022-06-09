a = str(input())
reverse_a = ''

for i in a:
    reverse_a = i + reverse_a

if (reverse_a == a):
    print(1)
else:
    print(0)
