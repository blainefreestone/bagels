def uppercaseDecorator(function):
    
    def wrapper():
        func = function()
        makeUppercase = func.upper()
        return makeUppercase
    
    return wrapper

def splitString(function):
    
    def wrapper():
        func = function()
        splittedString = func.split()
        return splittedString
    
    return wrapper

@splitString
@uppercaseDecorator
def sayHi():
    return 'hello there'

print(sayHi())