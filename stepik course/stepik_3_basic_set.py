#
# Множества set
#

s = set() # создание пустого множества 
obj =['apple', 'orange', 'beer','weesky']
basket={'apple','apple','apple','orange','flower','raspberry','cherry', 'popatos', 'tomato'}
print(basket)

if 'orange' in basket: # проверка вхождения элемента в множество   
	print('Orange in the basket')
else:
	print('There is no orange in the basket')

for i in range(len(obj)):
	if obj[i] in basket:
		print(' {} in the basket'.format(obj[i]))
	else:
		print('The object {} is not in the trash'.format(obj[i]))

'''
	Операции с множествами
	s.add(element)
	s.remove(element)
	s.discard(element)
	s.clear()
'''
# Перебор элементов множества
print('print all set() elemests:')
for x in basket: # выведет все элементы множества без повторов
	print(x, end=' ')


'''
Операции со словарями: dictionary = {key:value}
dict = {} пустой словарь
d = {a:10; b:20; c:30}
print(d['a'])

key in dictionary	  	#true/false
key not in dictionary	#true/false
dictionary[key]=value	# new value
dictionary[key]			# get value, если ключа нет то вызовет ошибку 
dictionary.get(key)		# get value, если ключа нет то вернет None
del dictionary[key]		# delete dictionary 

Перебор элементов словаря

d={'a':1, 'b':12, 'c':22, 'd':65, 1:21, 2:23, 3:42, 4:42}

for key in d:
	print(key, end='') # 

for key in d.keys():		# вывод всех ключей словаря
	print(key, end='') # 

for value in d.values():	# вывод всех значений словаря
	print(value, end='') # 	

for key, value in d.items():	# вывод всех пар ключ : значение
	print(key, value, end=';') # 	

'''

print()
d={'a':1, 'b':12, 'c':22, 'd':65, 1:21, 2:23, 3:42, 4:42}

for key in d:
	print(key, end='; ') # 
print()
for key in d.keys():		# вывод всех ключей словаря
	print(key, end='; ') # 
print()
for value in d.values():	# вывод всех значений словаря
	print(value, end='; ') # 	
print()
for key, value in d.items():	# вывод всех пар ключ : значение
	print(key, value, end='; ') # 	

