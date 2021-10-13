h,m = input().split()
h = int(h)
m = int(m)

if(m >= 45):
    print(h,m-45)
elif(m < 45 and h >0):
    print(h-1,m+15)
elif(h == 0 ):
    print(23, m+15)