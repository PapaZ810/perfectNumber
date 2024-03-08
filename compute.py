import math


def perfectNumber():
    for n in range(1, 500):
        n1 = 2**n - 1
        n2 = 2**(n-1)
        if isprime(n1):
            print("Number", n2*n1, "is a perfect number")


def isprime(n):
    if n < 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    perfectNumber()
