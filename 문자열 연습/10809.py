s = input()
abc = list(range(97, 123)) #아스키코드 알파벳 소문자 범위

for i in abc:
    print(s.find(chr(i)), end=" ")

##공부필