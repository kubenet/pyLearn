# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.

def modify_list(lst):
    d=[]
    print(len(lst))
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])
        if lst[i] % 2 != 0:
            d.append(i)
        else:
            lst[i] = lst[i] // 2 
    for i in range(len(d)):
        lst.pop(d[i])
    

def modify_list2(lst):
    for i in range(len(lst)-1,-1,-1):
        if lst[i] % 2 != 0:
            lst.pop(i)
            i=i+1
        else:
            lst[i] = lst[i] // 2


lst = [1, 2, 3, 4, 5, 6]
'''
d=[]

for i in reversed(range(len(lst))):
    print(lst[i])
    if lst[i] % 2 != 0:
        d.append(i)
    else:
        lst[i] = lst[i] // 2 
for i in range(len(d)):
    lst.pop(d[i])

print(lst)
'''
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
