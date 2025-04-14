#Ans 1
'''for i in range(1,51):
    if i%3==0 and i%5==0:
        print(i," FizzBuzz")
    elif i%3==0:
        print(i," Fizz")
    elif i%5==0:
        print(i," Buzz")'''

#Ans 2
'''num = int(input("Enter a number"))
if num>1:
    for i in range(2,(num//2)+1):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")
            break

else:
    print(num,"is not a prime number") '''


#Ans 3
'''while True:

    score = int(input("Enter the Score(to Ouit enter -1): "))
    if score>90 and score<100:
        print("A")
    elif score>80 and score<89:
        print("B")
    elif score>70 and score<79:
        print("C")
    elif score>60 and score<69:
        print("D")
    elif score<60 and score>0:
        print("F")
    elif score == -1:
        print("Quit")
        break '''
    
#Ans 4
'''num = int(input("Enter the Number whose table you want: "))
for i in range(1,11):
    print(f"{i}*{num} = {i*num}") '''

#Ans 5
'''li =[]
for i in range(1,20):
    if i%2==0:
        b = i**2
        li.append(b)
print(f"List of Square of even numbers:{li}") '''

#Ans 6
year = int(input("Enter the year(eg:-2024,1956 etc.): "))
a = str(year)
if len(a)==4:
    year = int(a)
    if year%4 ==0 or year%100==0 or year%400 == 0:
        print("Yes it is a leap year")
    else:
        print("It is not a leap year")
else:
    print("Invalid YearEntry") 

#Ans 7
'''li =[]
for i in range(3):
    a = int(input(f"Enter the side {i+1} of triangle: "))
    li.append(a)
li.sort()
if li[0]==li[1]==li[2]:
    print("Equilateral Triangle")
elif li[0]**2+li[1]**2 == li[2]**2:
    print("Right-angle triangle")
elif li[0]==li[1] or li[0]==li[2] or li[1]==li[2]:
    print("Isosceles Triangle")
elif li[0]!=li[1] or li[0]!=li[2] or li[1]!=li[2]:
    print("Scalene Triangle") '''

#Ans 8
'''num = int(input("Enter an integer number: "))
if num<0:
    print("Number is negative")
elif num>0:
    print("Number is positive")
elif num==0:
    print("Number is zero")'''

#Ans 9
'''pswd = input("Enter the password: ")
a = False
b = False
c = False
d = False
for i in pswd:
    if i.isupper():
            a = True
    elif i.islower():
            b = True
    elif i.isdigit():
            c =True
    elif i in "!@#$%^&*()":
            d = True
if len(pswd)<8:
    print("password must at least 8 characters long")
if a==False or b==False:
    print("Password must contain both uppercase and lowercase characters")
if c == False:
    print("Password must contain at least one digit")
if d==False:
    print("Password must contain at least one special character (e.g.!, @, #, $, etc.)")

if a and b and c and d:
    print("Strong password")
else: 
    print("Weak password") '''

#Ans 10
'''a = input("Enter Your weight(in kgs): ")
b = input("Enter your height(in metres): ")
wt = float(a)
ht = float(b)
bmi = wt/(ht**2)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<24.9:
    print("Normal weight")
elif bmi>=25 and bmi<29.9:
    print("Overweight")
elif bmi>=30:
    print("Obesity") '''

#Ans 11
'''day = int(input("Press any number between 1 to 12: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Input") '''

#Ans 12
'''cost = int(input("Enter the cost of product: "))
if cost>1000:
    discount = 0.10*cost
    print(f"After applying 10% discount: {discount}")
elif cost>500 and cost<1000:
    discount = 0.5*cost
    print(f"After applying 5% discount: {discount}")
elif cost<500:
    print(f"No discount applied: {cost}")'''

#Ans 13
'''n = int(input("Enter the range: "))
sum =0
for i in range(1,n+1):
    sum+=1

print(sum)'''

#Ans 14
'''li=[]
a = int(input("Enter the size of the list: "))
for i in range(a):
    li1=[]
    li1A = int(input(f"Enter the size of the list {i+1}: "))
    for i in range(li1A):
        b = int(input(f"Enter the {i+1} element: "))
        li1.append(b)
    li.append(li1)

print(li)'''

#Ans 15
'''a = input("Enter a string: ")
b = a.lower()
count = 0
aVowel= 0
eVowel = 0
iVowel = 0
oVowel = 0
uVowel = 0
for i in b:
    if i=="a" or i =="e" or i=="i" or i=="o" or i=="u":
        count+=1
        if i=="a":
            aVowel+=1
        elif i=="e":
            eVowel+=1
        elif i=="i":
            iVowel+=1
        elif i=="o":
            oVowel+=1
        else:
            uVowel+=1

print("Total vowels:",count)
print(f"a-{aVowel}\ne-{eVowel}\ni-{iVowel}\no-{oVowel}\nu-{uVowel}") '''

#Ans 16
'''a = input("Enter a number: ")
b = a.replace(".","")
sum = 0
for i in b:
    sum+=int(i)
print(sum)
'''

#Ans 17
'''n = int(input("Enter the range: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()'''

#Ans 18
'''import random as rn
print("Welcome To Number Guessing Game(:D)")
a = rn.randint(1,100)
while True:
    n = int(input("Guess an Integer Number between 1 to 100, or to Quit type -1: "))
    if n<100 and n>0:
        if n>a:
            print("Too High")
        elif n<a :
            print("Too Low")
        elif a==n:
            print("You Win")
    else:
        print("invalid range")
    if n ==-1:
        print("Thanks for playing")
        break'''

