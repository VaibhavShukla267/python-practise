mydict={
    "fast":"In a quick mannner",
    "vaibhav":"A Coder",
    "marks":[1,2,3,4],
    "anotherdict":{'vaibhav':'player'},
    1: 2
}

print(list(mydict.keys()))       #------------>prints the key sof dictonery
print(mydict.values())           #------------->prints the values of the keys in dictonery
print(mydict.items())             #----------->prints the keys as well as value for all contents in dictonery
print(mydict)
updatedict={                        #--------------->update the dictonery by adding key values pair 
    "utsav":"friend",
    "vishesh":"friend",
    "aman":"friend",
}
mydict.update(updatedict)
print(mydict)
#--------IMPORTANT-----------------#-------------difference get and simple printing of dictonery------#
print(mydict.get("vaibhav1"))      #----->if value is not there it will print none
#and if we use this
print(mydict("vaibhav1"))     #--------->this shows error 

print(mydict.get("vaibhav"))      #----->if value is not there it will print value
#and if we use this
print(mydict("vaibhav"))         #------->it will print value