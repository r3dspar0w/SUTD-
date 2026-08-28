#typecasting = the process of converting one value of one data type to another 


#Expliciting type casting - manual conversion 

name = "Meena"
age = 19
gpa = 4.0
student = True

'''print(type(name))
print(type(age))
print(type(gpa))
print(type(student))'''

age = float(age)

print(type(age))

age = str(age)

print(type(age))

age = bool(age)
print(type(age))
print(age) #output = True as long as it is non-zero

age = int(age)
print(type(age))
print(age) #output = 1

student = str(student)
print(student) #prints True 

#converting string to bool is useful to check if someone entered theirname or not

print(f"{name} + {bool(name)}")
#as long as there is no empty string it is True 

#Implicit 
x = 2 
y =2.0

x = x/y

print(x) #output of x is float