def fibonacci(n): 
    """
    fibonacci that calculate the fibonacci of numbers by using recursion
    e.x: the fibonacci number 2 is increasing the fibonacci number 1 and fibonacci number 0
    and note that the fibonacci 0 is 0 and fibonacci 1 is 1
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    lucas that calculate the lucas of numbers by using recursion
    e.x: the lucas number 2 is increasing the lucas number 1 and lucas number 0
    and note that the fibonacci 0 is 2 and fibonacci 1 is 1
    """
    if n==0:
        return 2
    elif n==1:
        return 1
    elif n>1:
        return lucas(n-1) + lucas(n-2)

def sum_series(n,first=0,sec=1):
    """
    this way make the input first number and sec number by default 0 and 1
    but I late the user to change these default value
    """
    if n==0:
        return first
    elif n==1:
        return sec
    else:
        return sum_series(n-1,first,sec) + sum_series(n-2,first,sec)


