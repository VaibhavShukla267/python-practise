def percent(mark):      #-------------def ka mtlab ye ek function hy--------#
    p=((mark[0]+mark[1]+mark[2]+mark[3])/400)*100
    return p  #---------return ka tlab laut chlo iss value ke sath -----------------#
mark1=[77,55,66,88]
percentage1=percent(mark1)


mark2=[99,88,77,66]
percentage2=percent(mark2)


print(percentage1,percentage2)