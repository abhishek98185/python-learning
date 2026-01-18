def avg(a,b,c):
    return a+b+c/3
print(avg(1,2,3))

#write a function to greet a user with "good day " using function 


#function defination 
def greet():
    print("Good Day !")

#function call 
greet()



#function with arguments 
def greets(name):
    print(f"Good morning {name }")
name=input("enter the name ")
greets(name)



#function with return value 

def sum(a,b):
    return a+b
add = sum(1,2)
print(add)



# default argument 

def sum(a,b=0):
    print(a+b)

sum(1,2)
sum(1)

