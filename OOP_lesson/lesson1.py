#
# Классы ООП
#

class Person:
    name = "None"
    age  = 0
    departmen = "None"
    salary = 0

    def __init__(self, name, age=0, salary=0):
        self.name 	= name
        self.age 	= age
        self.salary = salary

    def print_info_person(self):
        print(self.name +' is '+ str(self.age) +' age Departmen: '+ self.departmen+' Salary: '+str(self.salary))

    def setName(self, newName):
        self.name = newName

    def setAge(self, newAge):
        self.age = newAge

    def setDepartment(self, newDeparment):
        self.departmen = newDeparment

class Drive(Person):
    auto = ''
    auto_id = ''
    price = 0
    max_passenger = 5

    def __init__(self, auto = 'None', auto_id = 'None', price = 1000, max_passenger = 5):
        self.auto = auto
        self.auto_id = auto_id
        self.price = price
        self.max_passenger = max_passenger

    def print_info_drive(self):
        return self.auto, self.auto_id, self.price, self.max_passenger


Bob = Person('Bob', 23, 300)
Max = Person('Max',43)

Max.name = 'Max'
Max.age = 25
Max.departmen = 'IT'

Max.print_info_person() 
Bob.print_info_person()

Bob.setName('Den')
Bob.setAge(33)
Bob.setDepartment('Driver')
Bob.print_info_person() 

Dzho = Person('Mark', 27)
Dzho.print_info_person()
print('\n')

Ben = Drive('Golf', 'AD 007 70',4000, 7)
Ben.setName('Ben')
Ben.setAge(73)
Ben.salary = 8000
Ben.setDepartment('Bus Driver')

print(Ben.print_info_person())
print(Ben.print_info_drive())
