Q.1 write a program to check given number is prime or not:
flag = False
n=int(input("enter a number:"))
if n==0 or n==1:
    print(n,"is not a prime no.")
elif n>1:
    for i in range(2,n):
        if (n%i==0):
            flag=True
            break
if flag:
    print(n,"is not a prime no.")
else:
    print(n,"it is a prime no.")

Q.2 write a program to find whether given no. is palindrome or not
n=int(input("enter the no."))
old=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if old==rev:
    print("number is palindrome")
else: 
    print("number is not a palindrome")


Q.3 write a program to find grade of a student using given percentage

sub1=int(input("enter marks"))
sub2=int(input("enter marks"))
sub3=int(input("enter marks"))
sub4=int(input("enter marks"))
sub5=int(input("enter marks"))
per=(sub1+sub2+sub3+sub4+sub5)/5
if per>=90:
    print("grade assigned=A+")
elif per>=80 and per<90:
    print("grade assigned=A")
elif per>=70 and per<80:
    print("grade assigned=B+")
elif per>=60 and per<70:
    print("grade assigned=B")
elif per>=40 and per<60:
    print("grade assigned=C")
else:
    print("grade assigned=F")

Q.4 write a program to make a simple calculator

n1=int(input("enter first digit"))
n2=int(input("enter second digit"))
op=input("select your operation:+,-,*,//")
if op=='+':
    print(n1+n2)
elif op=='-':
    print(abs(n1-n2))
elif op=='*':
    print(n1*n2)
elif op=='//':
    print(n1//n2)
else:
    print("invalid operator")


Q.5 program to find sum of digits

num=(input("enter number:"))
sum=0 
for i in num: 
    sum=sum+int(i) 
print(sum)


Q.6   program to reverse a number
num = 9078
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Number: " + str(reversed_num))


--------LAB 2---------------
Q.1 WAP to generate fibonacci series

n=int(input("enter no. of terms:"))
n1=0
n2=1
count=0
if n<=0:
    print("enter positive integer:")
elif n==1:
    print(n1)
else:
    print("fibonacci series is:")
    while count<n:
        print(n1)
        n_th=n1+n2
        n1=n2
        n2=n_th
        count+=1

Q.2 wap to check for armstrong number
num=int(input("enter number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("valid")
else:
    print("invalid")

////Q.3 wap to check for strong number////
Q.4 wap to print multiplication tables

n=int(input("enter number:"))
for i in range(1,11):
    print(num*i)
----------------------------------------------
#wap to find factorial of any no. using reduce fn
import functools
def factorial(n):
    if n == 0:
        return 1
    else:
        return functools.reduce(lambda x,y: x*y, range(1,n+1))
num=int(input("enter number"))
print(factorial(num))


#wap to find largest among three no.s using reduce fn
import functools
list=[]
num=input("enter numbers")
for i in num:
    list.append(i)
result = functools.reduce(lambda x, y: x if x>y else y,list)
print(result)

----------LAB 4-------------
Q.2 To separate the following string into comma (,) separated values. X= “ India.is.my.country”
x='India.is.my.country'
y=x.split(".")
print(y)

# To remove a given character from a string. Y=”M.A.N.I.P.A.L” 
C. To remove the (.) dots from the above string.
x='India.is.my.country'
y=x.replace('.',' ')
print(y)


#Write a program to sort strings alphabetically in python. 

from functools import reduce

def sortString(input_str):
    # Split the input string into words
    words = input_str.split()

    # Sort the words alphabetically
    sorted_words = sorted(words)

    # Join the sorted words with a space between them
    return " ".join(sorted_words)

# Input from user
str_input = input("Enter a string that you want to arrange in alphabetical order: ")

# Call the function and print the result
print(sortString(str_input))

 
#Take an input from a user as a string then, reverse it.
string=input("enter string")
res=string[::-1]
print(res)

#Write a program to check if a string contains only digits.
# Get input from the user
string = input("Enter string: ")

# Flag to track if any digit is found
found_digit = False

# Check each character in the string
for i in string:
    if i in '0123456789':
        found_digit = True
        break 
if found_digit:
    print("yes")
else:
    print("no")

#Write a program to find the number of vowels in the string.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string:", vowel_count)


#WAP to take input of length of string then iterate through each element and cube each element
length = int(input("Enter the length of the string: "))
num_string = input("Enter a string ")
cubes = [int(char) ** 3 for char in num_string ]
print("Cubes of Each Element:", cubes)

#wap to check whether given string is palindrome

s=input("enter string")
palindrome=False
for i in s:
    if s[::-1]==s:
        palindrome=True
        break
if palindrome:
    print("yes,it is palindrome")
else:
    print("not palindrome")


Lab 4 : Pattern based Questions.
1.	Write a program to print the following pattern:-
Pattern #1: Simple Number Triangle Pattern
Pattern:
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
for i in range(1,6):
    print((str(i)+' ') *i)


Pattern #2: Inverted Pyramid of Numbers
Pattern:
1 1 1 1 1 
 2 2 2 2 
  3 3 3 
   4 4 
    5
n = 5  # number of rows

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')  # print spaces
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


Pattern #3: Half Pyramid Pattern of Numbers
Pattern:
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5
size = 5
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(i + 1):
        print(k + 1, end="")
    print()


Pattern #4: Inverted Pyramid of Descending Numbers
Pattern:
5 5 5 5 5 
  4 4 4 4 
    3 3 3 
      2 2 
       1

size = 5

for i in range(size, 0, -1):
    print(" " * (size - i), end="")
    print((str(i) + " ") * i)

Pattern #5: Inverted Pyramid of the Same Digit
Pattern:
5 5 5 5 5 
  5 5 5 5 
    5 5 5 
     5 5 
      5
digit = 5
levels = 5

for i in range(levels, 0, -1):
    print(" " * (levels - i), end="")
    print((str(digit) + " ") * i)

Pattern #6: Reverse Pyramid of Numbers
Pattern:
     1 
     2 1 
    3 2 1 
  4 3 2 1 
5 4 3 2 1

size = 5
for i in range(size, 0, -1):
    print(" " * (size - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print() 

Pattern #7: Inverted Half Pyramid Number Pattern
Pattern:
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1

size = 5
for i in range(size + 1):
    for j in range(size - i):
        print(j, end=" ")
    print() 


Pattern #8: Pyramid of Natural Numbers Less Than 10
Pattern:
1 
2 3 4 
5 6 7 8 9

number = 1
levels = 3
for i in range(1, levels + 1):
    for j in range(1, 2 * i):  
        if number < 10:  
            print(number, end=" ")
            number += 1
    print() 

Pattern #9: Reverse Pattern of Digits from 10 
Pattern:
1
3 2
6 5 4
10 9 8 7

levels = 4
current_number = 1

for i in range(1, levels + 1):
    last_number = current_number + i - 1
    for j in range(last_number, current_number - 1, -1):
        print(j, end=" ")
    current_number += i
    print()

Pattern #10: Unique Pyramid Pattern of Digits
Pattern:
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1

size = 5

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print() 

Pattern #11: Connected Inverted Pyramid Pattern of Numbers
Pattern:
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 2 3 4 5 
5 4 3 3 4 5 
5 4 4 5 
5 5

def connected_inverted_pyramid(n):
    for i in range(n):
        for j in range(n, i, -1):
            print(j, end=" ")
        for j in range(i+1, n):
            print(j+1, end=" ")
        print()

connected_inverted_pyramid(5)

Pattern #12: Even Number Pyramid Pattern
Pattern:
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2

def even_number_pyramid(n):
    for i in range(1, n+1):
        num = 10
        for j in range(i):
            print(num, end=" ")
            num -= 2
        print()

even_number_pyramid(5)


Pattern #13: Pyramid of Horizontal Tables
Pattern:
0  
0 1  
0 2 4  
0 3 6 9  
0 4 8 12 16  
0 5 10 15 20 25  
0 6 12 18 24 30 36

def pyramid_of_horizontal_tables(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(i * j, end=" ")
        print()

pyramid_of_horizontal_tables(6)


Pattern #14: Pyramid Pattern of Alternate Numbers
Pattern:
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9

def pyramid_of_alternate_numbers(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=" ")
        num += 2 
        print()

pyramid_of_alternate_numbers(5)


Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
Pattern:
 1 
         1 2 
      1 2 3 
   1 2 3 4 
 1 2 3 4 5

def mirrored_pyramid(n):
    for i in range(1, n+1):
        print(" " * (n - i) * 2, end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

mirrored_pyramid(5)

Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)
Pattern:
            *   
           * *   
          * * *   
         * * * *   
        * * * * *   
       * * * * * *   
      * * * * * * *

n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

Pattern #17: Downward Triangle Pattern of Stars
Pattern:
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('*', end='')
    print()


Pattern #18: Pyramid Pattern of Stars
Pattern:
* 
* * 
* * * 
* * * * 
* * * * *
rows = 5
for i in range(1, rows + 1):
    # Print i stars in the ith row
    for j in range(1, i + 1):
        print("*", end=" ")
    # Move to the next line after each row
    print()















