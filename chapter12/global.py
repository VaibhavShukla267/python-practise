a=54    #-------Global variable

def func1():
    global a
    print(a)
    a=8     #----Local varible---------if global keyword is not used
    print(a)
    
func1()
print(a)
    