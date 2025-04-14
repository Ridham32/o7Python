''' a = "Sahil1123@764. 12Hello"
for i in a:
    if i.isdigit():
        if int(i)%2 == 0:
            print(i) '''

#lists
a = [33,2.54,"hello",True,"bye",33,"list",12]
'''
print(li)
print(len(li))
print(a[4][1])
#or
b= a[4]
print(b[1])  '''

'''li=[33,2.54,["hello",True,["12345",False,22],"bye",33],"list",12]
print(li[2][2][0][2])
print(li[2][2][1]) '''

#Lists functions
a.append(["ridham",123,True])
a.append(2344)
print("Append func", a)

a.remove(33)
print("Remove func",a)

e = [1,7,5,4,0,3]
e.sort()
print("After Sorting in ascending order ", e)
e.sort(reverse = True)
print("Sorting in descending Order: ",e)

print("******************")
c = [33,"hello",True,8.90]
print("length of c: ",len(c))
print("Before Inserton: ",c)
c.insert(3,"daviet")  #(index where u want to insert, item u want to insert)  #doesn't replace
print("After Insertion: ",c)
print("length of c: ",len(c))

c.reverse()  #reverse in descending order 
print("After reversing List: ", c)



e.extend("hello")  #only takes string
print(e)

# e.clear()  #remove the elements in the list
# print(e)

print("copy list: ",e.copy())
#del(e) #remove the existence if the list





