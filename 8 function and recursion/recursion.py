def factorial(num):
    fact=1
    if num==1 or num ==0 :
        return fact
    fact=num*factorial(num-1)
    return fact
num=int(input("enter the number "))
fact=factorial(num)
print(fact)