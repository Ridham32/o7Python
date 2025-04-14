#Ans 1
'''abc = input("Enter a string: ")
c =""
for i in range(len(abc)):
    if i%2 ==0:
        c += abc[i].upper()
    else:
        c += abc[i].lower()
print(c)'''

#Ans 2
'''N = int(input("Enter a number: "))
def fib(n):
    if n <=0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(N)) '''

#Ans 3
'''li=[]
a = int(input("Enter the range of the list: "))
for i in range(a):
    c = int(input(f"Enter the {i+1} number: "))
    li.append(c)

def getList(lst):
    if type(lst) == list:
        lst.sort()
        print("Before: ",lst)
        
        for i in range(len(lst)-1,0,-1):
            if lst[i] == lst[i-1]:
                lst.remove(lst[i])
    else:
        print("not type list")
getList(li)
print("After eliminating Duplicates: ",li) '''
    
#Ans 4
'''n = int(input("enter an interger: "))
def sumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        if n<=0:
            print("Number should be a positive integer")
            break
        a = int(i)
        sum += a

    print("Sum is: ",sum) 
sumOfDigits(n) '''

#Ans 5
'''li = []
a = int(input("Enter the length of the list: "))
for i in range(a):
    c = int(input(f"Enter the {i+1} number: "))
    li.append(c)
def sortList(lst):
    if type(lst) == list:
        lst.sort()
        print("After Sorting: ",lst)
        num == 1
        if num == li[i]:
            num+=1
    else:
        print("Give List to sortList function")
sortList(li)
print("Smallest missing number is:", num)'''

#Ans 6
'''a = int(input("Enter the length of the list: "))
li = []
li1 =[]
li2=[]
for i in range(a):
    c = int(input(f"Enter the {i+1} number: "))
    li.append(c)
t = int(input("Target Sum: "))
for i in li:
    num = t-i
    if num in li:
        li1.append(i)
        li1.append(num)
    sets = set(li1)
    tpl = tuple(sets)
li2.append(tpl)
print(li2) '''

#Ans 7
a = int(input("Enter the length of the list: "))
li = []
for i in range(a):
    c = int(input(f"Enter the {i+1} number: "))
    li.append(c)
li.sort()
for i in li:
    if li.count(i)>=1:
        























