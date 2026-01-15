#1. write a program to find the largest of 4 numbers


#method 1  list method
lst=[]
for i in range (0,4):
    temp=int(input(f"enter the {i+1} number "))
    lst.append(temp)

print(max(lst))


#method 2 if else conditional statement
num1=int(input("enter the 1st number "))
num2=int(input("enter the 2nd number "))
num3=int(input("enter the 3rd number "))
num4=int(input("enter the 4th number "))

if num1>num2 :
    temp1=num1
else:
    temp1=num2

if num3>num4 :
    temp2=num3
else:
    temp2=num4

if temp1>temp2:
    print(f"the largest number is {temp1}")

else :
    print(f"the largest number is {temp2}")


#2. write a program to find wheather a student has passed or failed if it requires 
# a total of 40% and atleast 33% in each subject to pass .Assume 3 subject and take 
# marks as  an input  from user

marks1=int(input("enter the marks of first subject "))
marks2=int(input("enter the marks of second subject "))
marks3=int(input("enter the marks of third subject "))
if(marks1 >33 and marks2>33 and marks3>33 and marks1+marks2+marks3>120):
    print("student is passed")
else:
    print("student is failed")


#3 A spam comment is defined as a text containing following keyword 
#  "Makes a lots of money","buy now ","subscribe this ","click this" write a program to detect this spam



comment=input("enter the comment ")
spam_keyword=["makes a lots of money","buy now","subsecribe this","click this"]
for words in spam_keyword:
    if words in comment:
        print("the comment is spam ")
        break
else:
    print("the comment is not spam ")



#4. write a program to find wheather a given username contains less than 10 characters or not

username=input("enter the username ")
if len(username)<10 :
    print("yes! the username is less than 10 character ")
else:
    print("no! the username is not less than 10 character ")


#5. Find out whether a name is present in the list of not 

n=int(input("enter the number of name you want to enter "))
lst=[]
for i in range (n):
    temp=input("enter the name ")
    lst.append(temp)

name=input("enter the name you want to find ")
if lst.count(name)!=0:
    print("yes the name is present")
else:
    print("no the name is not present")


#6.Write a program to calculate the grade of the student from his marks from the following scheme
#     90-100 -Ex
#     80-90 -A
#   70-80 -B
#   60-70 -C
#   50-60 -D
#   <50  -F

marks=int(input("enter you marks "))
if(marks>=90 and marks <=100):
    print("EX")
elif(marks>=80):
    print("A")
elif(marks>=70):
    print("B")
elif(marks>=60):
    print("C")
elif(marks>=50):
    print("D")
else:
    print("F")


#write a program to find weather a given post is talking about abhishek or not

main_post=input("enter the post ")
post=main_post.lower()
if post.find("abhishek")>0:
    print("yes the post is about abhishek")
else:
    print("No! the post is not about abhishek")