# Программа вычисляет високосный год или нет

year=int(input())
if (year % 4 == 0) and not(year % 100 == 0) or (year % 400 == 0):
    print('Високосный')
else:
    print('Обычный')
    
