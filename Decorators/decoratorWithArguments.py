def decoratorWithArguments(function):

    def wrapperAcceptingArguments(arg1, arg2):
        print(f"My arguments are {arg1}, {arg2}")
        function(arg1, arg2)
    
    return wrapperAcceptingArguments

@decoratorWithArguments
def cities(cityOne, cityTwo):
    print(f"Cities I love are {cityOne} and {cityTwo}")

cities("Sacramento", "Santiago")