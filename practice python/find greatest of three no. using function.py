from unittest.util import _MIN_COMMON_LEN


def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
m=maximum(3,6,7)
print("The Of value of maximum number is"+str(m))

    
    