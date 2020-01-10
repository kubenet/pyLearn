'''
Сколько элементов будет содержать список students после следующих операций?

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'

Введите в поле ответа одно число.
Подумайте, почему так происходит.
'''
students = ['Ivan', 'Masha', 'Ivan', 'Sasha']
#print(students)

students += ['Olga']
#print(students)

#students += 'Olga'
#print(students)

students2 = ['Ivan','Egor','Igor','Sasha']
students3 = ['Ivan']
students3 *= 4
print('len = ', len(students), students, sep=' ')
print('len = ', len(students2), students2, sep=' ')
print('len = ', len(students3), students3, sep=' ')
for i in range(len(students2)):
        if students2[i] in students:
                print('Yes')
                print(students2[i][::-1])
        else:
                print('False')
