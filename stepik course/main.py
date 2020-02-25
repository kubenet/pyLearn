#1.8 Переменные. Стандартный ввод/вывод

x=int(input()) 
h=int(input())
m=int(input())
while(x>720):
    x=x-720

x=x+m
print((x//60)+h)
print(x%60)
