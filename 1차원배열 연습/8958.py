t = int(input())

for i in range(t):
    score = 0
    num = 0
    ox = input()
    for k in ox:
        if k == 'O':
            score += 1
        else:
            score = 0
        num += score
    print(num)
