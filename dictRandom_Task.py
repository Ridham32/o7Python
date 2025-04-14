import random as rn

#Ans1
'''
color = ["Black","Red","Maroon","Yellow"]
code = ["#000000","#FF0000","#800000","#FFFF00"]
result = [{"colorName":color[i],"colorCode":code[i]} for i in range(len(color))]

print(result)
'''
#Ans2
#Rock Paper Scissor
c = rn.choice(["Rock","Paper","Scissor"])
t = int(input("Enter the number of turns you want to play: "))
Uscore = 0
Cscore = 0
for i in range(t):
    f = input("Enter(Rock,Paper,Scissor): ")
    u = f.title()
    print("Your Choice: ",u)
    print("Computer Choice: ",c)
    if c==u:
        print()
    elif (c=="Scissor" and u=="Rock") or (c=="Rock" and u=="Paper") or (c=="Paper" and u=="Scissor"):
            Uscore+=1
    elif (c=="Rock" and u=="Scissor") or (c=="Paper" and u=="Rock") or (c=="Scissor" and u=="Paper"):
            Cscore+=1
    else:
        print("Invalid Option")
    print(f"Your Score: {Uscore} , Computer Score: {Cscore}")
    

if Uscore>Cscore:
    print("Hurray! You Win")
elif Uscore==Cscore:
    print("Its Draw")
else:
    print("Computer Win")




