# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

# Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
# Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

# Требуется реализовать только эту функцию, кода вне неё не должно быть.
# Функция не должна вызывать внутри себя функции input и print.

# Пример работы функции:

# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

s = set()

print(type(s))
s.add(1)
s.add(2)
s.add(3)

print(s)
l=list(s)
l.append(1)
l.append(2)
l.append(3)
l2 = l
l2.append(777)
print(l)
print(type(l))

print(l2)
print(type(l2))

d = {}
print(d)
print(type(d))

d[0]=1
d[2]=15
d[33]=14

d[33]=d[33],44,55
d[0]=d[0],l2
print(d)


