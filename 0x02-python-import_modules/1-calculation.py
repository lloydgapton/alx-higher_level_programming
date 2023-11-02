#!/usr/bin/python3
if _name_ == "_main_":
    """Performs basic calculations."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".fornmat(a,b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
