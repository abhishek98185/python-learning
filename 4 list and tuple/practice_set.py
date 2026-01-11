# 1.write a program to store seven fruits entered by user

lst=[]
for i in range (0,7):
    temp=input(f"enter the name for {i+1}th  fruit ")
    lst.append(temp)

print(lst)


#2.write a program to accept the marks of 6 student and display in sorted mannar

lst2=[]
for i in range(0,6):
    temp=int(input(f"enter the number of {i+1}th student "))
    lst2.append(temp)

print(sorted(lst2))

#3. Write a program to get sum of a list with 4 numbers 

lst3=[13,23,55,24]
print(sum(lst3))

#4 write a program to get the number of 0 in tuple (7,0,8,0,0,9)
tup=(7,0,8,0,0,9)
print(tup.count(0))