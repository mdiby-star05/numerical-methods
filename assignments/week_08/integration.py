# Students should edit this Python file (just as you would a Python cell in a Jupyter Notebook)
# this module will contain functions for numerical integration


def trapezoidal_rule():
    #write the arguments, docstring, and actual code of this function

    return



def simpsons_rule():
    #write the arguments, docstring, and actual code of this function

    return

# this module will contain functions for numerical integration

def trapezoidal_rule(f, a, b, N):
    """
    Approximate the integral of a function using the trapezoidal rule.

    Parameters:
    f : function
        The function to integrate
    a : float
        Lower limit of integration
    b : float
        Upper limit of integration
    N : int
        Number of slices

    Returns:
    float
        Approximate value of the integral
    """
    h = (b - a) / N
    
    total = 0.5 * (f(a) + f(b))
    
    for i in range(1, N):
        x = a + i * h
        total += f(x)
    
    return h * total



def simpsons_rule(f, a, b, N):
    """
    Approximate the integral of a function using Simpson's rule.

    Parameters:
    f : function
        The function to integrate
    a : float
        Lower limit of integration
    b : float
        Upper limit of integration
    N : int
        Number of slices (must be even)

    Returns:
    float
        Approximate value of the integral
    """
    if N % 2 != 0:
        raise ValueError("N must be even for Simpson's rule")
    
    h = (b - a) / N
    
    total = f(a) + f(b)
    
    for i in range(1, N):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)
    
    return (h / 3) * total