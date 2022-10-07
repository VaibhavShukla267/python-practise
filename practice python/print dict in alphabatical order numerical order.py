from operator import itemgetter


ages={'julian':20,'bob':23,'zack':3,'anthony':95,'daniel':41}
sort_key=itemgetter(0)
t=sorted(ages.items(),key=sort_key)
sort_key=itemgetter(1)
u=sorted(ages.items(),key=sort_key)
print(t)
print(u)