import math

def logDecorator(function):

    def wrapper(*args):
        for arg in args:
            arg = math.log(arg)
        
        func = function(args)
        logFunction = func
        return logFunction
    
    return wrapper