myDict = {
    'Hejsan': 'Hoppsan',
    'Hej': 'Svejs'
}

try:
    test = myDict['doesnt_exist']
except Exception as e: ## in python you can write just except: to catch any error, but to get a variable out of it like we do in C# the syntaax looks like this
    print('Exception caught', e.__class__)
    raise ## just typing raise and nothing else is similar to C# throw; just rethrows the exception
finally: 
    print('Finally block executed') ## finally works the same as in c#

class MyOwnException(Exception): ## just like in C# you can make your own exception by inheriting from Exception
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if (1 > 0):
    raise MyOwnException('Exception raised because I can!') ## raise is the keyword instead of throw
