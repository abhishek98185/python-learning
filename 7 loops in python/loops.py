#1. write a program to print elements in list using while loop and for loop
lst=eval(input("enter the list "))
i=0
while (i<len(lst)):
    print(lst[i])
    i+=1

for i in range (len(lst)):
    print(lst[i])