i = 1
while i>=1:
    budget = int(input("What is your budget(in USD) or to exit type -1: $"))
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
    
    elif budget == -1:
         print("Task completed")
         break
    
    else:
         print("Invalid Input")
    
    

            


