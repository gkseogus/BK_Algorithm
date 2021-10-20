a,b = map(int,input().split())
a_s = int(str(a)[::-1])
b_s = int(str(b)[::-1])

if (a_s > b_s):
    print(a_s)
else:
    print(b_s)