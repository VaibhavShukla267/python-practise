from os import remove


l1=[1,55,66,77,46,79,70]
l1.sort()
print(l1)
l1.reverse()
print(l1)      #-------->reverses the order
l1.append(69)  #-------->append means adds 69 to the end of list 
print(l1)
l1.insert(0,5444)        #--------------->inserts 5444 at index value of 0
print(l1)
#l1.pop(2)         #----------------->remove element of index 2
#print(l1)
l1.remove(77)  #------------------->removes 77 from lists
print(l1)
