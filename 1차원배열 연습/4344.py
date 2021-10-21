a = int(input())
for i in range(a):
    n = list(map(int, input().split()))
    avg = sum(n[1:])/n[0]
    cnt = 0
    for j in n[1:]:
        if j > avg :
            cnt += 1
    b = cnt / n[0] * 100
    print(f"{b:.3f}%")

    ##공부해야됨