#variables

age = 30 #integer

change = 3.50 #float

name = 'Stepan' #string

print(f'Hello, I am {name} and I am {age} years old. I have {change} dollars in my pocket.')

if age > 18:
    print('You are over the age of 18.')
else:
    print('You are under the age of 18.')

student = True #boolean

if age > 18 and student:
    print('You are a student over the age of 18.')
else:
    print('You are a student under the age of 18.')

#single line comment
"""Multiline comment
multi line comment"""

#define a function
def say_hello(name, age):
    return f'Hello World! My name is {name}. I am {age} years young.'
    
greeting = say_hello(name, age)

print(greeting, greeting)

#lists or arrays in other language such as javascript 

proteins = ['beef', 'chicken', 'eggs', 'fish', 'dairy']

print(proteins)

proteins.insert(0, 'wild game')

print(proteins)

print(proteins[0])

del(proteins[0])
print(proteins, len(proteins))

#for loop
for protein in proteins:
    print(protein)

for number in range(1, 11):
    print(number)
    
#while loop 

age = 15

def access(age):
    while age >= 18:
        print('Access granted')
    else:
        print('Access denied because you are under 18.')

access(age)

#dictionary

state_capitals = {
    'Colorado': 'Denver',
    'Montana': 'Helena',
    'Idaho': 'Boise',
    'Washington': 'Olympia',
}

print(state_capitals)
print(state_capitals['Colorado'])

state_capitals['California'] = 'Sacramento'
print(state_capitals)

removed_state_capital = state_capitals.pop('California')
del(state_capitals['Colorado'])
print(removed_state_capital)
print(state_capitals)

#classes 

class Dog:
    
    breed = 'German Shepherd'
    def bark(self):
        print('Bark, Bark!')

mydog = Dog()
mydog.bark()
mydog.name = 'Bison'
mydog.age = 5
print(mydog.name, mydog.age, Dog.breed)
        
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color 

mycat = Cat('Kocourek', 1, 'grey')
print(mycat.name, mycat.age, mycat.color)