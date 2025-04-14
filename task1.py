#Ans 1  
''' name = input("Enter Your Name")
age = int(input("Enter Your Age"))
college = input("Enter your college name")
print("Hello my name is "+ name +" having age "+ str(age) +" from "+ college )  '''

#Ans 2
'''a = 4
b = 4.5
c = True
d = "Ridham Sharma"
e = ["1","3.4","ridham",True]
print("Type of a: "+ str(type(a)))
print(f"Type of b: {type(b)}")
print(f"Type of c: {type(c)}")
print(f"Type of d: {type(d)}")
print(f"Type of e: {type(e)}")  '''

#Ans 3
''' name = input("Enter Your Name")
age = int(input("Enter Your Age"))
calcAge = 100 - age
print(f"My name is {name} having age {age} and i have {calcAge} years left to become 100 years old")  '''

#Ans 4
'''
a = int(input("Enter 1st number"))
b = int(input("Enter the second number"))
print(f"sum is: {a+b}")
print(f"Sub is: {a-b}")
print(f"Multiplication is: {a*b}")
print(f"Division is: {a/b}")    '''

#Ans 5
a = input("Enter a value")
print(f"Type of: {type(a)}")

try:
    float_a = float(a)
    print(f"Float value: {float_a}")
except ValueError:
    print("Cannot convert to float")

try:
    int_a = int(float_a)
    print(f"Int Value: {int_a}")
except ValueError:
    print("Cannot convert to integer")

bool_a = bool(a)
print(f"Boolean value: {bool_a}")