import math 


#area = pi * r^2 

radius = float(input("Enter your radius : "))
# area = math.pi * (radius ** 2)
area = math.pi * pow(radius, 2)

print(f"The area of your circle is {round(area, 3)} in 3 demical places")