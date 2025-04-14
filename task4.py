#Ans 1
''' a = input("Enter a string: ")
count = 0
for i in a:
    if i=="a" or i =="e" or i=="i" or i=="o" or i=="u":
        count+=1
print("Total vowels in the string:",count)  '''

#Ans 2
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

#Ans 3
''' a = input("Enter a string: ")
count = 0
aVowel= 0
eVowel = 0
iVowel = 0
oVowel = 0
uVowel = 0
for i in b:
    if i=="a" or i =="e" or i=="i" or i=="o" or i=="u":
        count+=1
        if i=="a" or i=="A":
            aVowel+=1
        elif i=="e" or i=="E":
            eVowel+=1
        elif i=="i" or i=="I":
            iVowel+=1
        elif i=="o" or i=="O":
            oVowel+=1
        elif i=="u" or i=="U":
            uVowel+=1
        else:
            print()

print("Total vowels:",count)
print(f"a-{aVowel}\ne-{eVowel}\ni-{iVowel}\no-{oVowel}\nu-{uVowel}") '''

#Ans 4
'''a = input("Enter a String: ")
count = 0
for i in range(len(a)):
    if a[i]=="a" or a[i]=="A":
        count+=1
        if count==2:
            print("2nd 'a' location is:-  ",i)
            break
if count==1:
    print("No 2nd Occurence of 'a'")    
elif count==0:
    print("'a' not found") '''

#Ans 5
'''a = input("Enter a string:")
b = a.lower()
c = b.rfind("i")
print(c) '''

#Ans 6
'''a = input("Enter a String:")
print("Total Character in string",len(a))
b=a.replace(" ","")
print("Total characters in string not inlcluded space",len(b))
count = 0
digitCount = 0
for i in a:
    if i == "a" or i== "A":
        count+=1
    if i.isdigit():
        digitCount+=1
print("Total character 'a' in the string: ",count)
print("Total digits in the string: ", digitCount)  '''

#Ans 7
'''a = int(input("Enter 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
if a>b and a>c:
    print("1st is greater number")
elif b>a and b>c:
    print("2nd is greater number")
else:
    print("3rd is greater number")  '''

#Ans 8
''' a = int(input("Enter a number: "))
if a%10==0 or a%5==0 or a%3==0:
    print("Allow")
else:
    print("Not Allowed") '''




