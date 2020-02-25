#Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

# На ввод могут подаваться и повторяющиеся числа.

# Sample Input 1:

# 8
# 2
# 14
# Sample Output 1:

# 14
# 2
# 8
# Sample Input 2:

# 23
# 23
# 21
# Sample Output 2:

# 23
# 21
# 23

lst=[]

x = int(input())
y = int(input())
z = int(input())

if (x >= y) and (x >= z):
    print(x)
elif (y >= x) and (y >= z):
    print(y)
elif (z >= x) and (z >= y):  
    print(z)

if (x <= y) and (x <= z):
    print(x)
elif (y <= x) and (y <= z):
    print(y)
elif (z <= x) and (z <= z):  
    print(z)

if (y <= x ) and (z >= x):
    print(x)
elif(y <=z ) and (x >= z):
    print(z)
    
elif (x <= y) and (z >= y):
    print(y)
elif (x <= z) and (y >= z):
    print(z)
    
elif (z <= x) and (y >= x):
    print(x)    
elif (z <= y) and (x >= y):
    print(y)
    

#lst.append(x)
#lst.append(y)
#lst.append(z)

#print(max(x,y,z))
#print(min(x,y,z))

#lst.remove(max(x,y,z))
#lst.remove(min(x,y,z))

#print(lst[0])

