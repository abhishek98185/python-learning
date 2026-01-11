l1=[34,23,42,11,34,55,66,32,45,66,42,53]
print(len(l1))
print(max(l1))
print(min(l1))
print(sum(l1))
print(sorted(l1))
average=sum(l1)/len(l1)
print(average)

l1.append(18)
print(l1)

l1.extend([18,45,77])
print(l1)
l1.insert(5,7)#insert 7 at 5th index
print(l1)
l1.remove(18)#remove first occuring of 18
print(l1)
print(l1.pop(4))#pop 4th index element and return the image
print(l1.pop())#by default pop last element
print(l1.count(18))