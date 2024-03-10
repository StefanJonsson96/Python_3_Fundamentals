import numbers


class Calculator:

    def __init__(self) -> None:
        pass ## pass is a placeholder keyword, so this is an empty constructor.

    def add(self, x, y):
        """Calculates the sum of two integers. ### Tripple quotes is code documentation, similar to C# /// syntax. 

    Args:
        x (int): The first integer to add.
        y (int): The second integer to add.

    Returns:
        int: The sum of x and y.

    Raises:
        TypeError: If either x or y is not an integer.""" 
        if type(x) is not int or type(y) is not int:
            raise TypeError('The function can only add integers.')
        return x + y


    print(add.__doc__) ## you can use the __doc__ syntax to get the code documentation in your code!
    ##print(add('hejsan', 2))