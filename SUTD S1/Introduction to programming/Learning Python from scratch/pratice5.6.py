import math 

# formula hypotenuse = sqrt(a^2 + b^2)

a = float(input("Enter length of side A :"))
b = float(input("Enter length of side B :"))

hypotenuse = math.sqrt(((pow(a,2))+ (pow(b,2))))

print(f"Side C is {hypotenuse}")