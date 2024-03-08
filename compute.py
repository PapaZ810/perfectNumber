from sympy import isprime
import sys

sys.set_int_max_str_digits(10000)


def perfectNumber():
    for n in range(1, 10000):
        n1 = 2**n - 1
        n2 = 2**(n-1)
        if isprime(n1):
            print("Number", n2*n1, "is a perfect number")


if __name__ == "__main__":
    perfectNumber()
