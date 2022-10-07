
#n!=n*(n-1)!
#n=5
# factorial=1
# for i in range(n):
#     factorial=factorial*(i+1)
# print(factorial)




# def factorial_iter(n):
#     factorial=1
#     for i in range(n):
#         factorial=factorial*(i+1)
#     return factorial
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1)

f=factorial_recursive(5)
print(f)