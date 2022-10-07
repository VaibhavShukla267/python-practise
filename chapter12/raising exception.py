from multiprocessing.sharedctypes import Value


def increment(num):
    try:
        return int(num) +1
    except:
        raise ValueError ("this is not goodd-vaibhav")

a=increment('dffe33')
print(a)