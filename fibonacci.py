def fibonacci_series():
    
    """
    This function generates de Fibonacci series
    between 0 to 50.
    """
    fibonacci = []
    i = 0
    
    while i < 50:
        if i == 0:
            fibonacci.append(0)
        elif i <= 1:
            fibonacci.append(1)
            fibonacci.append(1)
        i += 1
fibonacci_series()