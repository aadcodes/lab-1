#Q1
triple=lambda a : a*3
l1=[1,2,3,4,5]
l2=map(triple,l1)
print(list(l2))
#Q2
add4=lambda a,b,c,d : a+b+c+d
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
l3=[1,2,3,4,5]
l4=[1,2,3,4,5]
l5=map(add4,l1,l2,l3,l4)
print(list(l5))
#Q3
l1=["hello","how","are","you"]
l2=map(list,l1)
print(list(l2))
#Q4
import math
l1=[0,1,2,3,4]
l2=map((lambda a,n : math.pow(a,n)),l1,range(len(l1)))
print(list(l2))
#Q5
l1=[1,2,3,4]
square=map( (lambda a : a*a), l1)
print(list(square))
#Q6
l1=["H","E","e","l","L","o","o","H"]
l1=set(l1)
l2=filter(str.isupper,l1)
l3=filter(str.islower,l1)
print(list(l2))
print(list(l3))
#Q7
l1=[5,6,7,8]
l2=[1,2,3,4]
l3=map((lambda a,b : a-b),l1,l2)
print(list(l3))
#Q8
l=[5,6,7,8]
t=(1,2,3,4)
sl=map(str,l)
st=map(str,t)
print(list(sl))
print(list(st))
#Q9
l1=(9,8,7,5,4,3,2)
print(l1)
l2=[]
while(True):
    x=int(input("Enter position of elements to convert into string : "))
    l2.append(l1[x])
    choice=input("Do you want to enter more positions to convert to string (yes/no) : ")
    if (choice=="no"):
        break
l3=map(str,l2)
print(list(l3))
#Q10
n=int(input("Enter n : "))
a1=0
a2=1
print(a1," ",a2," ",end="")
l=[a1,a2]
for i in range (0,n-2):
    a3=a1+a2
    print(a3," ",end="")
    l.append(a3)
    a1=a2
    a2=a3
print("")
l1=map((lambda a : a*a ),l)
print(list(l1))
#Q11
import functools
arr=[1,2,3,4,5]
sum=functools.reduce((lambda a,b : a+b),arr)
print(sum)
