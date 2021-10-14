###########ver.1###########
list1 = []
for i in range(9):
    i = int(input())
    list1.append(i)
    
print(max(list1))
print(list1.index(max(list1))+1)


###########ver.2###########
# list1 = [input() for i in range(9)]
# max = list1[0]

# for k in list1[1:]:
#     if( k > max):
#         max = k

# print(max)
# print(list1.index(max)+1)


###########ver.3###########
# list1 = [input() for i in range(9)]
# print(max(list1))
# print(list1.index(max(list1))+1)