#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """list division  length

    Args:
        my_list_1: the first list
        my_list_2: the seond list
        list_length: the list length they want us to talk about

    Returns:
        return the new list
    """
    new_list = []
    div_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            div_list.append(result)
    return(div_list)
