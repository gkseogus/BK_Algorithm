a = int(input())

count = 0
while True:
    if (a >= 0):
        if (a % 5 == 0):
            count = count + (a//5)
            print(count)
            break
        a = a - 3
        count += 1
    else:
        print(-1)
        break
