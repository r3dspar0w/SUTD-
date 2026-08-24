#Data Types and variables 

#String variables
first_name = "Meena"
food = "pizza"
email = "meena@gmail.com"

#Integer varibles
age = 19
quantity = 3

#Float 
price = 10.99
gpa = 4.00

#Boolean
is_student = True



print(first_name)
print("first_name")

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

print(f"I am {age} years old")
print(f"We are buying {quantity} items")

print(price) #prints 10.99
print({price}) #print {10.99}
print(f"The price is {price}") #prints The price is 10.99

print(f"my GPA is {gpa}")

print(f"Are you a student?: {is_student}")

is_student = "bool"

print(f"Are you a student?: {is_student}")

print(type(is_student))

print(isinstance(is_student, (float, str) ))

