def remove_and_strip(string,word): #-strip removes blank spaces->
    newstr=string.replace(word,"")
    return newstr.strip()

this="   vaibhav is a coder   "
n=remove_and_strip(this,"vaibhav")
print(n)