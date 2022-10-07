try:
    i=int(input("Enter the Number:"))
    c=1/i
except Exception as e:
    print(e)
    exit()

finally:           #-----------finally ek aysi cheez hy jisme chaahe iske ek exit kyu lga ho tabhi iske neeche valla code execute hoga.
    print("We Are Done") #-----------it runs regardless of error------------------ 


        