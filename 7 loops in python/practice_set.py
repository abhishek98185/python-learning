#1.  Write a program to print multiplication table of a given number using for loop

# n=int(input("enter the number "))
# print("Printing table ")

# for i in range(1,11):
#     print(i*n)




#2.  Write a program to greet all the person names stored in a list 'l' and which start with S.
#     l=["Harry","Soham","Sachin","Rahul"]

# l=["Harry","Soham","Sachin","Rahul"]
# for i in l:
#     if(i[0]!="S"):
#         continue
#     else:
#         print("Good Morning "+i)




#3. Write a program to print multiplication table of a given number using while loop


# n=int(input("enter the number "))
# i=1
# while(i<11):
#     print(i*n)
#     i+=1

#4 write a program to find wheather a number is prime or not

# n=int(input("enter the number: "))
# for i in range (2,n):
#     if(n%i==0):
#         print("the number is not a prime number ")
#         break
#     else:
#         continue
# else:
#     print("the number is  a prime number")



#5. Write a program to find the sum of n natural number using while loop

# n=int(input("enter the value of n "))
# sum=0
# i=0
# while(i<n+1):
#     sum+=i
#     i+=1
# print("sum of n natural number is ",sum)




#6. write a program to find the factorial of a number using for loop

# n=int(input("enter the value of n "))
# fact=1
# i=1
# while(i<n+1):
#     fact*=i
#     i+=1
# print("the factorial of number n is ",fact)




#7.write the program to print the following start pattern.

#10. Write a program to print multiplication of a number n using for loop in reversed order 
n=int(input("enter the value of n "))
for i in range (10,0,-1):
    print(i*n)