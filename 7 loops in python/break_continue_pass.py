#break

for i in range(0,20):
    if (i==15):
        break           #break statement means that leave the loop after the break statement imediately
    print(i)
    


#continue

for i in range(0,20):
    if(i==15):
        continue    #skip the particular iteration and move to next value
    print(i)



#pass 

for i in range(0,10):
    pass # null statement in python generally used when we started a loop bt we will fix it later for now we have to just leave it

i=0
while (i<10):
    print(i)
    i+=1