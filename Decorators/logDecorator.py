import math

def logDecorator(function):

    def wrapper():
        func = function()
        logFunction = math.log(func)
        return logFunction
    
    return wrapper

@logDecorator
def square():
    return 4 * 4

print(square())