l=[] # временный список

d = {} # словарь
print(d)
print(type(d))

value = -1
key = 1

if key in d:
    l.append(value)
    d[key]=l
    
if key not in d:
    print('key not in d')
    if (key*2) in d:
        print('key*2 in d')
        l.append(d[key*2])
        l.append(value)
        d[key*2]=value
    else:
        print('key*2 not in d')
        d[key*2]=value

#print(l)
#print(d)

print(d) 
value = -2

if key in d:
    l.append(d[key])
    l.append(value)
    d[key]=l
    
elif key not in d:
    print('key not in d')
    if (key*2) in d:
        print('key*2 in d')
        l.append(d[key*2])
        l.append(value)
        d[key*2]=value
    else:
        print('key*2 not in d')
        d[key*2]=value
    

print(d) 
value = -3

if key in d:
    l.append(d[key])
    l.append(value)
    d[key]=l
    
elif key not in d:
    print('key not in d')
    if (key*2) in d:
        print('key*2 in d')
        l.append(d[key*2])
        l.append(value)
        d[key*2]=value
    else:
        print('key*2 not in d')
        d[key*2]=value
    
        
print(d) 
'''

def update_dictionary(d, key, value):
    l=[]
    if key in d:
        l.append(value)
        d[key]=l 
    elif ((key*2) not in d):
        d[2*key]=value
    else:
        d[2*key]=value
    
d = {}
print(update_dictionary(d, 2, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 2, -3)
print(d)                            # {2: [-1, -2, -3]}
'''
