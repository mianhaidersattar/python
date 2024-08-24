#problem1
print("Age Calculator")
birth_year = int(input("Enter your Birth-Year: "))
current_year = int(input("Enter your Current-Year: "))
print("Your age is ", (current_year - birth_year))

#problem2
print("Rectangle Area Calculator")
rectangle_length = int(input("Enter your Rectangle-length: "))
rectangle_width = int(input("Enter your Rectangle-Width: "))
print("The area of your rectangle is ", (rectangle_length * rectangle_width))

#problem3
print("Circle Area Calculator")
circle_radius = int(input("Enter your circle-radius: "))
pie_value = 3.1416
print("The area of the circle is: ", (pie_value * (circle_radius ** 2)))

#problem4
print("Cube Volume Calculator")
cube_length = int(input("Enter your Cube-Length: "))
cube_width  = int(input("Enter your Cube-Width: "))
cube_height = int(input("Enter your Cube-Height: "))
print("The volume of the Cube is: ", (cube_length * cube_width * cube_height))

#problem5
Print("\t Temperature Calculator")
print("Temperature Convertor (Celsius -> Fahrenheit)")
temperature = int(input("Enter your temperature in Celsius: "))
print("Temperature in Fahrenheit is: ", ((temperature * 9 / 5) + 32))
print("Temperature Convertor (Fahrenheit -> Celsius)")
temperature = int(input("Enter your temperature in Fahrenheit: "))
print("Temperature in Celsius is: ", ((temperature - 32) * 5 / 9))


#problem6
print("Time Calculator (Minutes -> Seconds)")
time_minutes = int(input("Enter your time in minutes: "))
print("Time in seconds is: ", (time_minutes * 60))


#problem7
print("Percentage Calculator")
percentage = int(input("Enter your percentage: "))
marks = int(input("Enter your marks: "))
print("Percentage is: ", ((percentage / 100) * marks))


#problem8
print("BMI Calculator")
weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print('Overweight')
else:
    print('Obesity')
    
    
    
#problem9 
    print("Cylinder Volume Calculator (V = πr²h)")
radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))
pie_value = 3.1416
print("Volume of Cylinder is: ", pie_value * (radius ** 2) * height)