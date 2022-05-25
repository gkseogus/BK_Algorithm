a = list(input().strip())

countNum = 0

if (2 <= len(a) <= 15):
    for i in range(len(a)):
        if(a[i] == 'W' or a[i] == 'X' or a[i] == 'Y' or a[i] == 'Z'):
            countNum += 10
        elif(a[i] == 'T' or a[i] == 'U' or a[i] == 'V'):
            countNum += 9
        elif(a[i] == 'P' or a[i] == 'Q' or a[i] == 'R' or a[i] == 'S'):
            countNum += 8
        elif(a[i] == 'M' or a[i] == 'N' or a[i] == 'O'):
            countNum += 7
        elif(a[i] == 'J' or a[i] == 'K' or a[i] == 'L'):
            countNum += 6
        elif(a[i] == 'G' or a[i] == 'H' or a[i] == 'I'):
            countNum += 5
        elif(a[i] == 'D' or a[i] == 'E' or a[i] == 'F'):
            countNum += 4
        elif(a[i] == 'A' or a[i] == 'B' or a[i] == 'C'):
            countNum += 3
        else:
            countNum += 2
    print(countNum)
