x = lambda a : a + 10
print(x(10))

x = lambda a, b : a * b
print(x(10,10))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))