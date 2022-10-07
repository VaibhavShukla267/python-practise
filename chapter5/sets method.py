#this syntax is used to create empty dictonery 
a={}
print(type(a))
#an empty set be made uing syntax bellow 
b=set()
print(type(b))
#addidng value to empty set #set is collection of non repetitive elmement isiliye print nhi krega same element
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add(4)
b.add(4)           #-------------addding a value repetitively we cannot chamge the vlues 
#b.add([4,5,6])   #------------>we cannot add list and dictonery in set
b.add((4,5,6))     #------------->we can add tupple to set

#b.add({4:5})    #------------>we cannot add list and dictonery in set
print(b)



print(len(b))   #-------->prints length of sets

#removing elements from set
b.remove(5)      #------------>removes 5 from set b
#b.remove(15)      #throws an errror while removing #because its not there in set b
print(b)