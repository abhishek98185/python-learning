#1.  Write a program  using functions to find greatest of three numbers 

# def maximum(a,b,c):
#     print(max(a,b,c))

# a=int(input("enter the first number: "))
# b=int(input("enter the second number: "))
# c=int(input("enter the third number: "))

# maximum(a,b,c)


#2. Write a pythob program using function to convert Celsius to Fahrenheit

# def ctof(celsius):
#     return (9/5 * celsius )+32

# celcius=int(input("enter the temprature in celsius: "))
# farenheit=ctof(celcius)
# print("equivalent temprature in fareheit is: ",farenheit)

#3. How do you prevent a python print() function to print a new line at the end 

# print("abhishek ",end="")
# print("abhishek")

 #4. write a recursive function to calculate the sum of first n natural numbers 

# sum=0
# def naturalsum(n):
#     global sum
#     if n==0:
#         return 0
#     sum=n+naturalsum(n-1)
#     return sum 

# n=int(input("enter the number "))
# print(naturalsum(n))

#5. write a python function to print first n lines of the following pattern 

# def pattern(n):
#     if n==0:
#         return
#     print("*" * n)
#     pattern(n-1)
# pattern(5)

#6.Write a python function which converts inches to cms. 
# def inchtocm(inch):
#     return 2.54*inch
# inch=int(input("enter the no of inch "))
# cm=inchtocm(inch)
# print("equivalent to cm ",cm)

#7. Write a python function to remove a given word from a list ad strip iy sy yhr dsmr yimr 


#8. Write a python function to print multiplication table of a given number 
def multiplication(n):
    for i in range (1,11):
        print(n*i)
    
multiplication(10)