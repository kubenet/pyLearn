

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']

s_students = sorted(students) # возвращает отсортированный список
print(s_students)
print(min(students))
print(students[0])

print(max(students))
print(students[-1])

students.sort() #сортировка списка (изменение порядка элементов)
print(students)

# функция reverse() позволяет поулчить список в обратном порядке
students.reverse()
print(students)

s_students = reversed(students) # возвращает отсортированный список
for s in s_students:
    print(s)

a = [1, 2, 3]
print(a)
b = a
b[0] = 20
b = [5, 6]
print(b)

