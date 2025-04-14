'''a = [33,2.54,"hello",13,True,"bye",44,"list",12]
for i in a:
    if type(i) ==int:
        if i%2==0:
            print(i) '''

li = []
x = int(input(("Enter the number of values: ")))
for i in range(x):
    b = input("Enter Value: ")
    if b.isdigit():
        b = int(b)
    elif b.replace(".","").isdigit():
        b = float(b)
    elif b=="True" or b == "False":
        if b=="True":
            b = True
        else:
            b = False
    li.append(b)
print(li)

#ZIP function
'''a = [2,4,5,6,7]
b = [4,5,6,7,8]
c =list(zip(a,b))
print(c)
d = ["hello",4.5,33,True,98,3,4,6,2]
e = list(zip(b,d))
print(e)
x = list(zip(a,b,d))
print(x) '''



