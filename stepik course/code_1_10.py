a=int(input())
b=int(input())
h=int(input())

if a <= b:
    if h >= a and h <= b:
        print('Это нормально')
    elif h < a:
        print('Недосып')
    else:
        print('Пересып')
