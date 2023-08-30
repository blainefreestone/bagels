def decorator(function):
    
    def wrapper(*args, **kwargs):
        print("Positional arguments are:", args)
        print("Keyword arguments are:", kwargs)
        function(*args)
    
    return wrapper

@decorator
def functionNoArgs():
    print("No arguments here")

@decorator
def functionWithArgs(a, b, c):
    print(a,b,c)

functionNoArgs()
functionWithArgs(1,2,3)