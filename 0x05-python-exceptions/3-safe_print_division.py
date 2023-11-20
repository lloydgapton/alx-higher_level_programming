#!/usr/bin/python3
def safe_print_division(a, b):
    """safe print list integers

    Args:
        my_list: the list
        x: the number of element to print

    Return:
        the real number of integer printed
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None

    finally:
        print("Inside result: {}".format(result))
        return(result)
