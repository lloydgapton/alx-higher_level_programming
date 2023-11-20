#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    prints = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            prints += 1
        except (ValueError, typeError):
            continue
    print()
    return prints
