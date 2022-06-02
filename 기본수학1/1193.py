a = int(input())

line = 1
diff = 0
fountain = 1
denominator = 1

while True:
    if a > line:
        a -= line
        line += 1
    else:
        break

diff = line - a + 1

if (line % 2 == 0):
    fountain = a
    denominator = diff
else:
    fountain = diff
    denominator = a

print(fountain, '/', denominator, sep='')
