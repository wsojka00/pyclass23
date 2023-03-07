def check_prime(num):
    """Function which determine whether a number is a prime number.
    
    Input:
    num(int): number
    
    Output:
    True or False"""
    
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True