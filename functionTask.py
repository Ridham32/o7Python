#Ans 1
'''def conversion(temp):
    fahrenhit = (celsius*9/5) + 32
    return fahrenhit

celsius = float(input("Enter the temperature in celsius: "))
fahrenhitTemp = conversion(celsius)
print(f"{celsius}celsius is equal to {fahrenhitTemp} fahrenhit")'''

#Ans 2
'''num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
def gCD(a,b):
    smaller = min(a,b)
    gcd = 1
    for i in range(1,smaller+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    return i

a = gCD(num1,num2)
print(a)
'''

#Ans 3
'''def mergeList(lst1,lst2):
    for i in lst1:
        lst2.append(i)
    lst2.sort()
    return lst2

a = mergeList([6,3,9,2],[4,9,0,2,6,7,5])
print(a) '''

#Ans 4
'''def count_vowels(word):
    count =0
    word.lower()
    for i in word:
        if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
            count+=1
    return count

a = count_vowels("Ridham Sharma")
print(a)'''

#Ans 5
'''def largestNum(lst):
    lst.sort()
    a = set(lst)
    b = list(a)
    print("Second Largest Number is: ",b[len(b)-2])

list1 = [6,3,8,2,9,1,5,7,6,3,5]
largestNum(list1)'''

#Ans 6
'''def removeDuplicates(lst):
    a = set(lst)
    b = list(a)
    print(f"After removing duplicates: {b}")

lst1 = [5,5,7,3,8,9,2,5,2,2,6,7]
removeDuplicates(lst1) '''

#Ans 7
'''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Checking only up to sqrt(n)
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    prime_sum = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

n = int(input("Enter the range: "))
print(f"Sum of prime numbers up to {n} is {sum_of_primes(n)}.")
'''

#Ans 8
'''def isLeapYear(year):
    a = str(year)
    if len(a)==4:
        year = int(a)
        if year%4 ==0 or year%100==0 or year%400 == 0:
            print("Yes it is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("Invalid YearEntry")

yr = int(input("Enter the year(eg:-2024,1956 etc.): "))
isLeapYear(yr)'''

#Ans 9
def reverse_words(sentence):
    words = sentence.split() 
    reversed_sentence = " ".join(reversed(words)) 
    return reversed_sentence

# Example usage
sentence = input("Enter a sentence: ")
print("Reversed sentence:", reverse_words(sentence))




        
            
            
        
            
            