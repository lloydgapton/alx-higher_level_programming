#!/usr/bin/python3
def safe_print_integer(value):
    """safe print integer
    Args:
    value: the value must be int
    Returns:
    return true and otherwise False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except:
        return (False)
