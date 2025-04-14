#Ans 1
'''li =["hello",56,4.67,True]
print(li)'''

#Ans 2
'''li = [1,10,100,3,6,8]
li.insert(3,59)
li.append(5)
print(li)
print("Length of the list:",len(li))  '''

#Ans 3
'''li=[]
for i in range(10) :
        b = int(input("Enter the value: "))
        li.append(b)
print(li)
for i in range(len(li)):
    if li[i]%2==0:
        print(i,end=" ")    '''

#Ans 4
'''li = ["Gaurav",12,23,33.33,"Sharma",True]
for i in li:
    if type(i)==str:
        print(i) '''

#Ans 5
'''li = ["Gaurav",12,23,33.33,"Sharma",True]
sum = 0
for i in li:
    if type(i)==int or type(i)==float:
        sum = sum+i
print("Sum of all numbers present in the list: ",sum) '''

#Ans 6
'''friendList = [1,2,"harpreet",4,5]
name = input("Enter the name of your friend: ")
friendList.append(name)
print(friendList)
imptName = input("Enter name of your important friend: ")
valueIndex = int(input(f"Locaton of the index for {imptName}: "))
friendList.pop(valueIndex)
friendList.insert(valueIndex,imptName)
print(friendList) '''
