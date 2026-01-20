import random
computer=random.choice(["stone","paper","scissor"])
you=input("enter stone/paper/scissor ")
print("you enterend: ",you)
print("computer chose: ",computer)
if(you==computer):
    print("Draw! Play again ")

else:
    if(you=="stone" and computer=="paper"):
        print("You Loose! ")
    
    elif(you=="stone" and computer=="scissor"):
        print("You won! ")
    
    elif(you=="paper" and computer=="stone"):
        print("You won! ")
    
    elif(you=="paper" and computer=="scissor"):
        print("You Loose! ")
    
    elif(you=="scissor" and computer=="stone"):
        print("You Loose! ")
    
    elif(you=="scissor" and computer=="paper"):
        print("You won! ")
    
    else:
        print("Something Wrong happen Try next time ")
    