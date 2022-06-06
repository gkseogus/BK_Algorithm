def check(n):
    if(n > 1):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True


x, y = map(int, input().split())

for i in range(x, y+1):
    if check(i):
        print(i)
