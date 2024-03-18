def multiply(a, b):
    return a * b


print(multiply(1, 2))
print(multiply(3, 5))


def is_prime(nr):
    """
    Verify if a number is prime
    nr - integer number, nr>1
    return True if nr is prime, False otherwise
    """
    div = 2   # search for divider starting from 2
    while div < nr and nr % div > 0:
        div = div + 1
    # if the first divider is the number itself than the number is prime
    return div >= nr


print(is_prime(6))
