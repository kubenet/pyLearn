# генерация списков

a = [0] * 5
print(a)

b = [1, 2, 3] * 3
print(b)

c = [0 for i in range(5)] #генерация списка из 5 нулей
print(c)

d = [i for i in range(5)] #генерация списка из 5 чисел
print(d)

e = [i**i for i in range(5)] #генерация списка из 5 нулей
print(e)

f = [2**i for i in range(5)] #генерация списка чисел в степени 2
print(f)
x=0


'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки. ﻿﻿

Sample Input:

4 -1 9 3
Sample Output:

15
'''

g = [int(i) for i in input().split()] # генерация списка чисел из строки ввода
sum1=  [x + g[i] for i in range(len(g))]
print(g)
print(sum1)

print(sum(g))

