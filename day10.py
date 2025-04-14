#List comprehension..... was Absent

# li = [i for i in range(10)]
# print(li)

# li = [i for i in range(5) if i<10]
# print(li)

#print this if this orint this if this

li = [i*i if i%2==0 else i for i in range(10)]
print(li)

li = ["name" for i in range(6)]
print(li)


li = [j for i in range (5) for j in range(5)]
print(li)
