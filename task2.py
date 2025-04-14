#Ans 1
''' month = int(input("Press any number between 1 to 12: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December") 
else:
    print("Invalid Input") '''

#Ans 2
'''a = int(input("Enter 1st number: "))
b = int(input("Enter the 2nd number: "))
print("Equality: ",a==b)

if a>b:
    print("1st number is greater than 2nd number")
    i = 1
    while i<=5:
        print("Ridham")
        i+=1
elif a<b:
    print("2nd number is greater than 1st number")
    j = 1
    while j<=3:
        print("Sharma")
        j+=1
else:
    print("both numbers are equal") '''


#Ans 3
'''a = input("Enter the 1st String: ")
b = input("Enter the 2nd String: ")
print(id(a),id(b))
print("Equality check using 'is' operator: ",a is b)  #check the Id
print("Equality check using '==' operator: ", a==b) '''


#Ans 4
'''a = input("Enter the 1st String: ")
b = input("Enter the 2nd String: ")
try:
    intValue1 = int(a)
    intValue2 = int(b)
    print(f"After converting to integer: 1st-{intValue1}, {type(intValue1)}\n2nd-{intValue2}, {type(intValue2)}")
    print("Identity check:", intValue1 is intValue2)
except ValueError:
    print("Can't convert to integer") '''



#Ans 5
'''budget = int(input("What is your budget(in USD) or to exit type -1: $"))
if budget >= 5000:
    print(f"Countries you can visit under {budget} budget")
    i = int(input("Press 1 for Germany \nPress 2 for Australia \nPress 3 for Malaysia\n"))
    if i == 1:
     print("Places to visit in Germany \nBerlin \nHamburg \nMunich")
    elif i == 2:
     print("Places to visit in Australia \nSydney \nMelbourne \nGreat Barrier Reef")
    elif i == 3:
     print("Places to visit in Malaysia \nKuala Lumpur \nPetaling Jaya \nKlang")
    else:
     print("Invalid Number Choosen")

elif budget <=5000:
    print(f"Countries you can visit under {budget} budget")
    i = int(input("Press 1 for India \nPress 2 for Vietnam \nPress 3 for China\n "))
    if i == 1:
     print("Places to visit in India \nDelhi \nMumbai \nKerala")
    elif i == 3:
     print("Places to visit in China \nBiejing \nShanghai  \nWuhan")
    elif i == 2:
     print("Places to visit in Vietnam \nHaNoi \nHai Phong \nCan Tho")
    else:
     print("Invalid Number Choosen")
    
else:
   print("Invalid Input")  '''