n_num = set(range(1,10001)) #1~10000까지 숫자 저장
g_num = set() #생성자 수 저장
for i in range(1,10001): 
    for j in str(i): #123 -> 1, 2, 3
        i += int(j) #123+1+2+3
    g_num.add(i) #셀프 넘버가 아닌 수 저장

#전체숫자 - 셀프넘버 아닌 수 
s_num = n_num - g_num
for i in sorted(s_num):
    print(i)